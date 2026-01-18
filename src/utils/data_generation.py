"""
Data Generation Utilities for Predator-Prey Supermodeling

Generates ground-truth trajectories and samples observations for training.
"""

import numpy as np
from dataclasses import dataclass

from src.models.lotka_volterra import (
    LotkaVolterraParams,
    solve_lotka_volterra,
    GROUND_TRUTH_PARAMS
)


@dataclass
class TrajectoryData:
    """Container for trajectory data."""
    t: np.ndarray           # Time points
    prey: np.ndarray        # Prey population x(t)
    predator: np.ndarray    # Predator population y(t)

    @property
    def y(self) -> np.ndarray:
        """Return as 2D array [prey, predator]."""
        return np.vstack([self.prey, self.predator])


@dataclass
class Observations:
    """Container for observed data (subsampled trajectory)."""
    t: np.ndarray           # Observation time points
    prey: np.ndarray        # Observed prey values
    predator: np.ndarray    # Observed predator values

    @property
    def y(self) -> np.ndarray:
        """Return as 2D array [prey, predator]."""
        return np.vstack([self.prey, self.predator])

    def __len__(self) -> int:
        return len(self.t)


def generate_ground_truth(
    params: LotkaVolterraParams,
    t_train: tuple[float, float],
    t_test: tuple[float, float],
    y0: np.ndarray,
    n_points: int = 200
) -> tuple[TrajectoryData, TrajectoryData]:
    """
    Generate ground-truth trajectories for training and test intervals.

    Args:
        params: Model parameters (ground truth)
        t_train: (t_start, t_end) for training interval
        t_test: (t_start, t_end) for test/prediction interval
        y0: Initial conditions [x0, y0]
        n_points: Number of points per interval for smooth trajectory

    Returns:
        train_trajectory: Ground truth on training interval
        test_trajectory: Ground truth on test interval
    """
    # Training trajectory
    t_eval_train = np.linspace(t_train[0], t_train[1], n_points)
    t_train_full, y_train = solve_lotka_volterra(params, t_train, y0, t_eval_train)
    train_trajectory = TrajectoryData(
        t=t_train_full,
        prey=y_train[0],
        predator=y_train[1]
    )

    # Test trajectory (use end of training as initial condition)
    y0_test = np.array([y_train[0, -1], y_train[1, -1]])
    t_eval_test = np.linspace(t_test[0], t_test[1], n_points)
    t_test_full, y_test = solve_lotka_volterra(params, t_test, y0_test, t_eval_test)
    test_trajectory = TrajectoryData(
        t=t_test_full,
        prey=y_test[0],
        predator=y_test[1]
    )

    return train_trajectory, test_trajectory


def sample_observations(
    trajectory: TrajectoryData,
    n_samples: int,
    noise_std: float = 0.0,
    seed: int | None = None
) -> Observations:
    """
    Subsample observations from a trajectory.

    Args:
        trajectory: Full trajectory data
        n_samples: Number of observation points to sample
        noise_std: Standard deviation of Gaussian noise to add (0 = no noise)
        seed: Random seed for reproducibility

    Returns:
        Observations with subsampled time points and values
    """
    if seed is not None:
        np.random.seed(seed)

    n_points = len(trajectory.t)
    if n_samples > n_points:
        raise ValueError(f"Cannot sample {n_samples} points from {n_points} available")

    # Sample indices uniformly (with some spacing to avoid clustering)
    indices = np.sort(np.random.choice(n_points, size=n_samples, replace=False))

    t_obs = trajectory.t[indices]
    prey_obs = trajectory.prey[indices].copy()
    predator_obs = trajectory.predator[indices].copy()

    # Add observation noise if specified
    if noise_std > 0:
        prey_obs += np.random.normal(0, noise_std, size=n_samples)
        predator_obs += np.random.normal(0, noise_std, size=n_samples)
        # Ensure non-negative populations
        prey_obs = np.maximum(prey_obs, 0.01)
        predator_obs = np.maximum(predator_obs, 0.01)

    return Observations(t=t_obs, prey=prey_obs, predator=predator_obs)


def generate_experiment_data(
    y0: np.ndarray = np.array([10.0, 5.0]),
    t_train: tuple[float, float] = (0.0, 15.0),
    t_test: tuple[float, float] = (15.0, 25.0),
    n_observations: int = 10,
    noise_std: float = 0.1,
    seed: int = 42
) -> tuple[TrajectoryData, TrajectoryData, Observations]:
    """
    Convenience function to generate complete experiment data.

    Args:
        y0: Initial conditions [prey, predator]
        t_train: Training time interval
        t_test: Test/prediction time interval
        n_observations: Number of observation points (~2-3× parameters)
        noise_std: Observation noise level
        seed: Random seed

    Returns:
        train_truth: Ground truth trajectory on training interval
        test_truth: Ground truth trajectory on test interval
        observations: Noisy observations sampled from training trajectory
    """
    train_truth, test_truth = generate_ground_truth(
        params=GROUND_TRUTH_PARAMS,
        t_train=t_train,
        t_test=t_test,
        y0=y0
    )

    observations = sample_observations(
        trajectory=train_truth,
        n_samples=n_observations,
        noise_std=noise_std,
        seed=seed
    )

    return train_truth, test_truth, observations
