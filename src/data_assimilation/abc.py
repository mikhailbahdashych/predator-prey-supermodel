"""
Approximate Bayesian Computation (ABC) for Parameter Estimation

Implements rejection-ABC algorithm for learning parameters of dynamical systems.
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Callable

from src.utils.data_generation import Observations


@dataclass
class Prior:
    """Uniform prior distribution for parameters."""
    low: np.ndarray   # Lower bounds for each parameter
    high: np.ndarray  # Upper bounds for each parameter

    def sample(self, n_samples: int = 1) -> np.ndarray:
        """Sample from uniform prior."""
        n_params = len(self.low)
        return np.random.uniform(
            self.low,
            self.high,
            size=(n_samples, n_params)
        )

    @property
    def n_params(self) -> int:
        return len(self.low)


@dataclass
class ABCResult:
    """Results from ABC parameter estimation."""
    best_params: np.ndarray           # Best parameter estimate
    best_distance: float              # Distance of best estimate
    accepted_params: np.ndarray       # All accepted parameter samples
    accepted_distances: np.ndarray    # Distances for accepted samples
    n_evaluations: int                # Total model evaluations (budget used)
    n_accepted: int                   # Number of accepted samples


def compute_distance(
    simulated: np.ndarray,
    observed: Observations,
    t_sim: np.ndarray,
    metric: str = "mse"
) -> float:
    """
    Compute distance between simulated trajectory and observations.

    Args:
        simulated: Simulated trajectory [2, n_times]
        observed: Observations object
        t_sim: Time points of simulation
        metric: Distance metric ("mse" or "rmse")

    Returns:
        Distance value (lower is better)
    """
    # Interpolate simulated values at observation times
    sim_at_obs = np.zeros((2, len(observed)))

    for i, t_obs in enumerate(observed.t):
        # Find nearest simulation time index
        idx = np.argmin(np.abs(t_sim - t_obs))
        sim_at_obs[:, i] = simulated[:, idx]

    # Compute distance
    diff = sim_at_obs - observed.y

    if metric == "mse":
        return np.mean(diff ** 2)
    elif metric == "rmse":
        return np.sqrt(np.mean(diff ** 2))
    else:
        raise ValueError(f"Unknown metric: {metric}")


def abc_rejection(
    model_fn: Callable[[np.ndarray], tuple[np.ndarray, np.ndarray]],
    observations: Observations,
    prior: Prior,
    n_particles: int,
    epsilon: float | None = None,
    n_accept: int = 100,
    seed: int | None = None,
    verbose: bool = False
) -> ABCResult:
    """
    ABC rejection sampling algorithm.

    Algorithm:
    1. Sample parameters from prior distribution
    2. Simulate model with sampled parameters
    3. Compute distance to observations
    4. Accept if distance < threshold ε (or keep best n_accept)
    5. Repeat until budget exhausted

    Args:
        model_fn: Function that takes params array and returns (t, y) trajectory
        observations: Observed data to fit
        prior: Prior distribution for parameters
        n_particles: Maximum number of model evaluations (budget)
        epsilon: Distance threshold for acceptance (if None, keep best n_accept)
        n_accept: Number of samples to accept (used if epsilon is None)
        seed: Random seed
        verbose: Print progress

    Returns:
        ABCResult with best parameters and statistics
    """
    if seed is not None:
        np.random.seed(seed)

    accepted_params = []
    accepted_distances = []
    all_distances = []
    all_params = []

    for i in range(n_particles):
        # Sample from prior
        params = prior.sample(1)[0]

        # Simulate model
        try:
            t_sim, y_sim = model_fn(params)

            # Compute distance
            distance = compute_distance(y_sim, observations, t_sim)
            all_distances.append(distance)
            all_params.append(params)

            # Accept/reject based on epsilon
            if epsilon is not None:
                if distance < epsilon:
                    accepted_params.append(params)
                    accepted_distances.append(distance)
            else:
                accepted_params.append(params)
                accepted_distances.append(distance)

        except Exception:
            # Simulation failed (e.g., unstable parameters)
            all_distances.append(np.inf)
            all_params.append(params)

        if verbose and (i + 1) % 1000 == 0:
            best_so_far = min(all_distances)
            print(f"  ABC: {i + 1}/{n_particles} evaluations, best distance: {best_so_far:.6f}")

    # Convert to arrays
    all_params = np.array(all_params)
    all_distances = np.array(all_distances)

    if epsilon is None:
        # Keep best n_accept samples
        sorted_idx = np.argsort(all_distances)[:n_accept]
        accepted_params = all_params[sorted_idx]
        accepted_distances = all_distances[sorted_idx]
    else:
        accepted_params = np.array(accepted_params) if accepted_params else np.zeros((0, prior.n_params))
        accepted_distances = np.array(accepted_distances) if accepted_distances else np.array([])

    # Find best
    if len(accepted_distances) > 0:
        best_idx = np.argmin(accepted_distances)
        best_params = accepted_params[best_idx]
        best_distance = accepted_distances[best_idx]
    else:
        # No accepted samples - return best from all
        best_idx = np.argmin(all_distances)
        best_params = all_params[best_idx]
        best_distance = all_distances[best_idx]

    return ABCResult(
        best_params=best_params,
        best_distance=best_distance,
        accepted_params=accepted_params,
        accepted_distances=accepted_distances,
        n_evaluations=n_particles,
        n_accepted=len(accepted_distances)
    )


def abc_smc(
    model_fn: Callable[[np.ndarray], tuple[np.ndarray, np.ndarray]],
    observations: Observations,
    prior: Prior,
    n_particles: int,
    n_generations: int = 5,
    alpha: float = 0.5,
    seed: int | None = None,
    verbose: bool = False
) -> ABCResult:
    """
    ABC Sequential Monte Carlo (more efficient than rejection).

    Uses adaptive thresholds and importance sampling for better efficiency.

    Args:
        model_fn: Model simulation function
        observations: Observed data
        prior: Prior distribution
        n_particles: Particles per generation
        n_generations: Number of SMC generations
        alpha: Quantile for threshold adaptation
        seed: Random seed
        verbose: Print progress

    Returns:
        ABCResult with best parameters
    """
    if seed is not None:
        np.random.seed(seed)

    total_evaluations = 0
    particles_per_gen = n_particles // n_generations

    # Initial generation - sample from prior
    params_list = []
    distances = []

    for _ in range(particles_per_gen):
        params = prior.sample(1)[0]
        try:
            t_sim, y_sim = model_fn(params)
            dist = compute_distance(y_sim, observations, t_sim)
        except Exception:
            dist = np.inf
        params_list.append(params)
        distances.append(dist)
        total_evaluations += 1

    params_array = np.array(params_list)
    distances = np.array(distances)

    # Keep best particles
    sorted_idx = np.argsort(distances)[:max(1, int(alpha * particles_per_gen))]
    params_array = params_array[sorted_idx]
    weights = np.ones(len(params_array)) / len(params_array)

    if verbose:
        print(f"  ABC-SMC Gen 0: {total_evaluations} evals, best: {distances[sorted_idx[0]]:.6f}")

    # Subsequent generations
    for gen in range(1, n_generations):
        epsilon = np.percentile(distances[sorted_idx], alpha * 100)

        new_params = []
        new_distances = []

        # Perturbation kernel (covariance from current particles)
        cov = 2 * np.cov(params_array.T) + 1e-6 * np.eye(prior.n_params)

        attempts = 0
        while len(new_params) < particles_per_gen and attempts < particles_per_gen * 10:
            # Sample from weighted particles
            idx = np.random.choice(len(params_array), p=weights)
            params = params_array[idx]

            # Perturb
            params = np.random.multivariate_normal(params, cov)

            # Check prior bounds
            if np.any(params < prior.low) or np.any(params > prior.high):
                attempts += 1
                continue

            try:
                t_sim, y_sim = model_fn(params)
                dist = compute_distance(y_sim, observations, t_sim)
                total_evaluations += 1

                if dist < epsilon:
                    new_params.append(params)
                    new_distances.append(dist)
            except Exception:
                total_evaluations += 1

            attempts += 1

        if new_params:
            params_array = np.array(new_params)
            distances = np.array(new_distances)
            weights = np.ones(len(params_array)) / len(params_array)

        if verbose:
            best_dist = np.min(distances) if len(distances) > 0 else np.inf
            print(f"  ABC-SMC Gen {gen}: {total_evaluations} evals, best: {best_dist:.6f}")

    # Return best
    if len(distances) > 0:
        best_idx = np.argmin(distances)
        return ABCResult(
            best_params=params_array[best_idx],
            best_distance=distances[best_idx],
            accepted_params=params_array,
            accepted_distances=distances,
            n_evaluations=total_evaluations,
            n_accepted=len(distances)
        )
    else:
        return ABCResult(
            best_params=prior.sample(1)[0],
            best_distance=np.inf,
            accepted_params=np.zeros((0, prior.n_params)),
            accepted_distances=np.array([]),
            n_evaluations=total_evaluations,
            n_accepted=0
        )
