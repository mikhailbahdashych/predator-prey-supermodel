"""
Lotka-Volterra (Predator-Prey) ODE Model

Classic predator-prey dynamics:
    dx/dt = alphax - betaxy   (prey growth - predation)
    dy/dt = deltaxy - gammay   (predator growth from predation - death)

Where:
    x = prey population
    y = predator population
    alpha = prey birth rate
    beta = predation rate
    delta = predator efficiency (conversion of prey to predator)
    gamma = predator death rate
"""

import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass


@dataclass
class LotkaVolterraParams:
    """Parameters for the Lotka-Volterra model."""
    alpha: float  # prey birth rate
    beta: float   # predation rate
    delta: float  # predator efficiency
    gamma: float  # predator death rate

    def to_array(self) -> np.ndarray:
        return np.array([self.alpha, self.beta, self.delta, self.gamma])

    @classmethod
    def from_array(cls, arr: np.ndarray) -> "LotkaVolterraParams":
        return cls(alpha=arr[0], beta=arr[1], delta=arr[2], gamma=arr[3])


# Ground-truth parameters
GROUND_TRUTH_PARAMS = LotkaVolterraParams(
    alpha=1.0,    # prey birth rate
    beta=0.1,     # predation rate
    delta=0.075,  # predator efficiency
    gamma=1.5     # predator death rate
)


def lotka_volterra(t: float, state: np.ndarray, params: LotkaVolterraParams) -> np.ndarray:
    """
    ODE right-hand side for Lotka-Volterra system.

    Args:
        t: Current time (not used, but required by ODE solver)
        state: [x, y] where x = prey, y = predator
        params: Model parameters

    Returns:
        [dx/dt, dy/dt]
    """
    x, y = state

    dx_dt = params.alpha * x - params.beta * x * y
    dy_dt = params.delta * x * y - params.gamma * y

    return np.array([dx_dt, dy_dt])


def solve_lotka_volterra(
    params: LotkaVolterraParams,
    t_span: tuple[float, float],
    y0: np.ndarray,
    t_eval: np.ndarray | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """
    Integrate the Lotka-Volterra system using scipy.

    Args:
        params: Model parameters
        t_span: (t_start, t_end) integration interval
        y0: Initial conditions [x0, y0]
        t_eval: Time points at which to store the solution

    Returns:
        t: Time points
        y: Solution array of shape (2, len(t)) where y[0] = prey, y[1] = predator
    """
    sol = solve_ivp(
        fun=lambda t, state: lotka_volterra(t, state, params),
        t_span=t_span,
        y0=y0,
        t_eval=t_eval,
        method='RK45',
        dense_output=True
    )

    return sol.t, sol.y
