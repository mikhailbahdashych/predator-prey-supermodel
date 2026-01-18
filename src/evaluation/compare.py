"""
Evaluation and Comparison Module

Compares prediction quality between baseline, surrogate, and supermodel.
"""

import numpy as np
from dataclasses import dataclass

from src.models.lotka_volterra import (
    LotkaVolterraParams,
    solve_lotka_volterra,
    GROUND_TRUTH_PARAMS
)
from src.models.supermodel import Supermodel
from src.training.surrogate1 import TrainedSurrogate
from src.utils.data_generation import TrajectoryData


@dataclass
class ModelMetrics:
    """Metrics for a single model."""
    name: str
    mse_train: float      # MSE on training interval
    mse_test: float       # MSE on test/prediction interval
    rmse_train: float     # RMSE on training interval
    rmse_test: float      # RMSE on test/prediction interval
    budget_used: int      # Model evaluations used


@dataclass
class ComparisonResults:
    """Results comparing all models."""
    baseline: ModelMetrics
    surrogate1: ModelMetrics
    submodels: list[ModelMetrics]
    supermodel: ModelMetrics

    def print_summary(self):
        """Print comparison table."""
        print("\n" + "=" * 80)
        print("MODEL COMPARISON RESULTS")
        print("=" * 80)
        print(f"{'Model':<35} {'MSE Train':>12} {'MSE Test':>12} {'Budget':>10}")
        print("-" * 80)

        for m in [self.baseline, self.surrogate1] + self.submodels + [self.supermodel]:
            print(f"{m.name:<35} {m.mse_train:>12.6f} {m.mse_test:>12.6f} {m.budget_used:>10}")

        print("-" * 80)
        print("\nKey insights:")

        # Compare surrogate1 vs supermodel
        if self.supermodel.mse_test < self.surrogate1.mse_test:
            improvement = (self.surrogate1.mse_test - self.supermodel.mse_test) / self.surrogate1.mse_test * 100
            print(f"  - Supermodel outperforms Surrogate 1 by {improvement:.1f}% on test set")
        else:
            degradation = (self.supermodel.mse_test - self.surrogate1.mse_test) / self.surrogate1.mse_test * 100
            print(f"  - Surrogate 1 outperforms Supermodel by {degradation:.1f}% on test set")

        # Budget comparison
        print(f"  - Surrogate 1 budget: {self.surrogate1.budget_used}")
        print(f"  - Supermodel total budget: {self.supermodel.budget_used}")
        print(f"  - Budget constraint satisfied: {self.supermodel.budget_used <= self.surrogate1.budget_used}")

        # Best individual submodel
        best_sub = min(self.submodels, key=lambda s: s.mse_test)
        print(f"  - Best individual submodel: {best_sub.name} (MSE test: {best_sub.mse_test:.6f})")


def compute_mse(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """Compute Mean Squared Error."""
    return np.mean((y_pred - y_true) ** 2)


def compute_rmse(y_pred: np.ndarray, y_true: np.ndarray) -> float:
    """Compute Root Mean Squared Error."""
    return np.sqrt(compute_mse(y_pred, y_true))


def evaluate_model(
    name: str,
    params: LotkaVolterraParams,
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    y0: np.ndarray,
    budget_used: int
) -> ModelMetrics:
    """
    Evaluate a single Lotka-Volterra model.

    Args:
        name: Model name
        params: Model parameters
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        y0: Initial conditions
        budget_used: Model evaluations used in training

    Returns:
        ModelMetrics
    """
    # Evaluate on training interval
    t_train, y_train = solve_lotka_volterra(
        params,
        (train_truth.t[0], train_truth.t[-1]),
        y0,
        train_truth.t
    )

    mse_train = compute_mse(y_train, train_truth.y)
    rmse_train = compute_rmse(y_train, train_truth.y)

    # Evaluate on test interval (use end of training as initial condition)
    y0_test = np.array([y_train[0, -1], y_train[1, -1]])
    t_test, y_test = solve_lotka_volterra(
        params,
        (test_truth.t[0], test_truth.t[-1]),
        y0_test,
        test_truth.t
    )

    mse_test = compute_mse(y_test, test_truth.y)
    rmse_test = compute_rmse(y_test, test_truth.y)

    return ModelMetrics(
        name=name,
        mse_train=mse_train,
        mse_test=mse_test,
        rmse_train=rmse_train,
        rmse_test=rmse_test,
        budget_used=budget_used
    )


def evaluate_supermodel(
    supermodel: Supermodel,
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    y0: np.ndarray
) -> ModelMetrics:
    """
    Evaluate the supermodel.

    Args:
        supermodel: Trained supermodel
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        y0: Initial conditions

    Returns:
        ModelMetrics
    """
    # Evaluate on training interval
    t_train, y_train = supermodel.solve(
        (train_truth.t[0], train_truth.t[-1]),
        y0,
        train_truth.t
    )

    mse_train = compute_mse(y_train, train_truth.y)
    rmse_train = compute_rmse(y_train, train_truth.y)

    # Evaluate on test interval
    y0_test = np.array([y_train[0, -1], y_train[1, -1]])
    t_test, y_test = supermodel.solve(
        (test_truth.t[0], test_truth.t[-1]),
        y0_test,
        test_truth.t
    )

    mse_test = compute_mse(y_test, test_truth.y)
    rmse_test = compute_rmse(y_test, test_truth.y)

    return ModelMetrics(
        name="Supermodel (Coupled)",
        mse_train=mse_train,
        mse_test=mse_test,
        rmse_train=rmse_train,
        rmse_test=rmse_test,
        budget_used=supermodel.total_budget
    )


def compare_models(
    surrogate1: TrainedSurrogate,
    submodels: list[TrainedSurrogate],
    supermodel: Supermodel,
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    y0: np.ndarray
) -> ComparisonResults:
    """
    Compare all models against ground truth.

    Args:
        surrogate1: Fully trained surrogate
        submodels: Partially trained submodels
        supermodel: Trained supermodel
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        y0: Initial conditions

    Returns:
        ComparisonResults
    """
    # Baseline (ground truth evaluated against itself = 0)
    baseline = evaluate_model(
        "Baseline (Ground Truth)",
        GROUND_TRUTH_PARAMS,
        train_truth,
        test_truth,
        y0,
        budget_used=0
    )

    # Surrogate 1
    surr1_metrics = evaluate_model(
        surrogate1.name,
        surrogate1.params,
        train_truth,
        test_truth,
        y0,
        budget_used=surrogate1.abc_result.n_evaluations
    )

    # Individual submodels
    sub_metrics = []
    for s in submodels:
        m = evaluate_model(
            s.name,
            s.params,
            train_truth,
            test_truth,
            y0,
            budget_used=s.abc_result.n_evaluations
        )
        sub_metrics.append(m)

    # Supermodel
    super_metrics = evaluate_supermodel(
        supermodel,
        train_truth,
        test_truth,
        y0
    )

    return ComparisonResults(
        baseline=baseline,
        surrogate1=surr1_metrics,
        submodels=sub_metrics,
        supermodel=super_metrics
    )
