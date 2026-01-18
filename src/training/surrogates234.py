"""
Surrogate Models 2, 3, 4 - Partial Pretraining via ABC

These submodels are trained with reduced budgets and different random seeds,
leading to diverse parameter estimates that will be combined in the supermodel.
"""

import numpy as np
from dataclasses import dataclass

from src.models.lotka_volterra import LotkaVolterraParams
from src.data_assimilation.abc import abc_rejection
from src.training.surrogate1 import (
    TrainedSurrogate,
    get_lotka_volterra_prior,
    create_model_fn
)
from src.utils.data_generation import Observations


@dataclass
class SubmodelsResult:
    """Container for all pretrained submodels."""
    submodels: list[TrainedSurrogate]
    total_budget_used: int


def train_submodels(
    observations: Observations,
    y0: np.ndarray,
    t_span: tuple[float, float],
    n_submodels: int = 3,
    budget_per_submodel: int = 2500,
    base_seed: int = 100,
    verbose: bool = True
) -> SubmodelsResult:
    """
    Train multiple submodels with partial budgets for supermodeling.

    Each submodel uses a different random seed to ensure diversity
    in the parameter estimates.

    Args:
        observations: Training observations
        y0: Initial conditions
        t_span: Time span for simulation
        n_submodels: Number of submodels to train (default 3)
        budget_per_submodel: Model evaluations per submodel
        base_seed: Base random seed (each submodel gets base_seed + i)
        verbose: Print progress

    Returns:
        SubmodelsResult with all trained submodels
    """
    if verbose:
        print(f"\nTraining {n_submodels} submodels with {budget_per_submodel} evaluations each...")
        print(f"Total pretraining budget: {n_submodels * budget_per_submodel}")

    prior = get_lotka_volterra_prior()
    model_fn = create_model_fn(y0, t_span, n_points=50)

    submodels = []
    total_budget = 0

    for i in range(n_submodels):
        submodel_num = i + 2  # Submodels are numbered 2, 3, 4, ...
        seed = base_seed + i

        if verbose:
            print(f"\n  Training Submodel {submodel_num} (seed={seed})...")

        result = abc_rejection(
            model_fn=model_fn,
            observations=observations,
            prior=prior,
            n_particles=budget_per_submodel,
            epsilon=None,
            n_accept=50,
            seed=seed,
            verbose=verbose
        )

        params = LotkaVolterraParams.from_array(result.best_params)
        total_budget += result.n_evaluations

        if verbose:
            print(f"    Parameters: alpha={params.alpha:.4f}, beta={params.beta:.4f}, "
                  f"delta={params.delta:.4f}, gamma={params.gamma:.4f}")
            print(f"    Best distance: {result.best_distance:.6f}")

        submodels.append(TrainedSurrogate(
            params=params,
            abc_result=result,
            name=f"Submodel {submodel_num} (Partial Training)"
        ))

    if verbose:
        print(f"\n  Total pretraining budget used: {total_budget}")
        print("\n  Parameter diversity across submodels:")
        for s in submodels:
            p = s.params
            print(f"    {s.name}: alpha={p.alpha:.4f}, beta={p.beta:.4f}, delta={p.delta:.4f}, gamma={p.gamma:.4f}")

    return SubmodelsResult(
        submodels=submodels,
        total_budget_used=total_budget
    )
