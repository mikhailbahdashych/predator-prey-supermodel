"""
Supermodel Training - Learning Coupling Coefficients via ABC

This module learns the 12 coupling coefficients that synchronize the
3 pretrained submodels in the supermodel.
"""

import numpy as np

from src.models.supermodel import (
    CouplingCoefficients,
    Supermodel,
    solve_supermodel
)
from src.data_assimilation.abc import (
    Prior,
    ABCResult,
    abc_rejection
)
from src.training.surrogate1 import TrainedSurrogate
from src.utils.data_generation import Observations


def get_coupling_prior(c_range: float = 1.0, positive_only: bool = True) -> Prior:
    """
    Get prior distribution for coupling coefficients.

    Args:
        c_range: Range for uniform prior
        positive_only: If True, constrain to [0, c_range] for stability.
                      Positive coupling = diffusive/synchronizing = stable.
                      Negative coupling can cause instability/divergence.

    Returns:
        Prior for 12 coupling coefficients
    """
    if positive_only:
        return Prior(
            low=np.full(12, 0.0),
            high=np.full(12, c_range)
        )
    else:
        return Prior(
            low=np.full(12, -c_range),
            high=np.full(12, c_range)
        )


def create_supermodel_fn(
    submodels: list[TrainedSurrogate],
    y0: np.ndarray,
    t_span: tuple[float, float],
    n_points: int = 200
):
    """
    Create a model function for ABC that optimizes coupling coefficients.

    Args:
        submodels: List of 3 pretrained submodels
        y0: Initial conditions
        t_span: Time span
        n_points: Points in trajectory

    Returns:
        Function that takes coupling array and returns (t, y_consensus)
    """
    t_eval = np.linspace(t_span[0], t_span[1], n_points)
    submodel_params = [s.params for s in submodels]

    def model_fn(coupling_array: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        coupling = CouplingCoefficients.from_array(coupling_array)
        t, y_consensus, _ = solve_supermodel(
            submodel_params, coupling, t_span, y0, t_eval
        )
        return t, y_consensus

    return model_fn


def train_supermodel_coupling(
    submodels: list[TrainedSurrogate],
    observations: Observations,
    y0: np.ndarray,
    t_span: tuple[float, float],
    pretraining_budget: int,
    budget: int = 2500,
    c_range: float = 1.0,
    seed: int = 200,
    verbose: bool = True
) -> Supermodel:
    """
    Train coupling coefficients for the supermodel via ABC.

    Args:
        submodels: 3 pretrained submodels
        observations: Training observations
        y0: Initial conditions
        t_span: Time span
        pretraining_budget: Budget already used for pretraining
        budget: Budget for coupling training
        c_range: Prior range for coupling coefficients
        seed: Random seed
        verbose: Print progress

    Returns:
        Trained Supermodel with optimized coupling
    """
    if verbose:
        print(f"\nTraining supermodel coupling coefficients...")
        print(f"  Coupling budget: {budget} evaluations")
        print(f"  Pretraining budget: {pretraining_budget}")
        print(f"  Total supermodel budget: {budget + pretraining_budget}")

    prior = get_coupling_prior(c_range=0.5, positive_only=True)  # Positive coupling for stability
    model_fn = create_supermodel_fn(submodels, y0, t_span, n_points=50)

    result = abc_rejection(
        model_fn=model_fn,
        observations=observations,
        prior=prior,
        n_particles=budget,
        epsilon=None,
        n_accept=50,
        seed=seed,
        verbose=verbose
    )

    coupling = CouplingCoefficients.from_array(result.best_params)

    if verbose:
        print(f"\n  Learned coupling coefficients:")
        print(f"    Prey (Cx):     12={coupling.Cx_12:.4f}, 13={coupling.Cx_13:.4f}, "
              f"21={coupling.Cx_21:.4f}, 23={coupling.Cx_23:.4f}, "
              f"31={coupling.Cx_31:.4f}, 32={coupling.Cx_32:.4f}")
        print(f"    Predator (Cy): 12={coupling.Cy_12:.4f}, 13={coupling.Cy_13:.4f}, "
              f"21={coupling.Cy_21:.4f}, 23={coupling.Cy_23:.4f}, "
              f"31={coupling.Cy_31:.4f}, 32={coupling.Cy_32:.4f}")
        print(f"  Best distance: {result.best_distance:.6f}")

    return Supermodel(
        submodels=submodels,
        coupling=coupling,
        training_budget=result.n_evaluations,
        total_budget=pretraining_budget + result.n_evaluations
    )
