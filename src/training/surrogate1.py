"""
Surrogate Model 1 - Full Training via ABC

This module trains a single Lotka-Volterra model using the full computational budget
via ABC parameter estimation.
"""

import numpy as np
from dataclasses import dataclass

from src.models.lotka_volterra import (
    LotkaVolterraParams,
    solve_lotka_volterra
)
from src.data_assimilation.abc import (
    Prior,
    ABCResult,
    abc_rejection
)
from src.utils.data_generation import Observations


@dataclass
class TrainedSurrogate:
    """Container for a trained surrogate model."""
    params: LotkaVolterraParams
    abc_result: ABCResult
    name: str


def get_lotka_volterra_prior() -> Prior:
    """
    Get prior distribution for Lotka-Volterra parameters.

    Ground truth: α=1.0, β=0.1, δ=0.075, γ=1.5
    Prior is centered around reasonable ranges.
    """
    return Prior(
        low=np.array([0.5, 0.05, 0.025, 0.5]),    # [α_min, β_min, δ_min, γ_min]
        high=np.array([2.0, 0.2, 0.15, 3.0])      # [α_max, β_max, δ_max, γ_max]
    )


def create_model_fn(y0: np.ndarray, t_span: tuple[float, float], n_points: int = 200):
    """
    Create a model function suitable for ABC.

    Args:
        y0: Initial conditions
        t_span: Time span for simulation
        n_points: Number of points in simulation

    Returns:
        Function that takes params array and returns (t, y) trajectory
    """
    t_eval = np.linspace(t_span[0], t_span[1], n_points)

    def model_fn(params_array: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        params = LotkaVolterraParams.from_array(params_array)
        t, y = solve_lotka_volterra(params, t_span, y0, t_eval)
        return t, y

    return model_fn


def train_surrogate1(
    observations: Observations,
    y0: np.ndarray,
    t_span: tuple[float, float],
    budget: int = 10000,
    seed: int = 42,
    verbose: bool = True
) -> TrainedSurrogate:
    """
    Train Surrogate Model 1 with full computational budget.

    Args:
        observations: Training observations
        y0: Initial conditions
        t_span: Time span for simulation
        budget: Maximum number of model evaluations
        seed: Random seed
        verbose: Print progress

    Returns:
        TrainedSurrogate with optimized parameters
    """
    if verbose:
        print(f"Training Surrogate 1 with budget = {budget} evaluations...")

    prior = get_lotka_volterra_prior()
    model_fn = create_model_fn(y0, t_span)

    result = abc_rejection(
        model_fn=model_fn,
        observations=observations,
        prior=prior,
        n_particles=budget,
        epsilon=None,  # Keep best samples
        n_accept=100,
        seed=seed,
        verbose=verbose
    )

    params = LotkaVolterraParams.from_array(result.best_params)

    if verbose:
        print(f"  Best parameters: α={params.alpha:.4f}, β={params.beta:.4f}, "
              f"δ={params.delta:.4f}, γ={params.gamma:.4f}")
        print(f"  Best distance: {result.best_distance:.6f}")
        print(f"  Total evaluations: {result.n_evaluations}")

    return TrainedSurrogate(
        params=params,
        abc_result=result,
        name="Surrogate 1 (Full Training)"
    )
