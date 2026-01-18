"""
Supermodel - Coupled Ensemble of Lotka-Volterra Submodels

The supermodel couples 3 partially-trained submodels through connection terms
that synchronize their dynamics. The coupling coefficients are learned via ABC.

Coupled ODE system for 3 submodels (k = 1, 2, 3):
    dx_k/dt = f_x(x_k, y_k, theta_k) + sum_{j!=k} C^x_{kj}(x_j - x_k)
    dy_k/dt = f_y(x_k, y_k, theta_k) + sum_{j!=k} C^y_{kj}(y_j - y_k)

Supermodel output (consensus):
    x_s = (x_1 + x_2 + x_3) / 3
    y_s = (y_1 + y_2 + y_3) / 3
"""

import numpy as np
from scipy.integrate import solve_ivp
from dataclasses import dataclass

from src.models.lotka_volterra import LotkaVolterraParams, lotka_volterra
from src.training.surrogate1 import TrainedSurrogate


@dataclass
class CouplingCoefficients:
    """
    Coupling coefficients for 3 submodels.

    For prey (x): C^x_{12}, C^x_{13}, C^x_{21}, C^x_{23}, C^x_{31}, C^x_{32}
    For predator (y): C^y_{12}, C^y_{13}, C^y_{21}, C^y_{23}, C^y_{31}, C^y_{32}

    Total: 12 coefficients
    """
    # Prey coupling coefficients
    Cx_12: float  # Coupling from submodel 2 to submodel 1 (prey)
    Cx_13: float  # Coupling from submodel 3 to submodel 1 (prey)
    Cx_21: float  # Coupling from submodel 1 to submodel 2 (prey)
    Cx_23: float  # Coupling from submodel 3 to submodel 2 (prey)
    Cx_31: float  # Coupling from submodel 1 to submodel 3 (prey)
    Cx_32: float  # Coupling from submodel 2 to submodel 3 (prey)

    # Predator coupling coefficients
    Cy_12: float  # Coupling from submodel 2 to submodel 1 (predator)
    Cy_13: float  # Coupling from submodel 3 to submodel 1 (predator)
    Cy_21: float  # Coupling from submodel 1 to submodel 2 (predator)
    Cy_23: float  # Coupling from submodel 3 to submodel 2 (predator)
    Cy_31: float  # Coupling from submodel 1 to submodel 3 (predator)
    Cy_32: float  # Coupling from submodel 2 to submodel 3 (predator)

    def to_array(self) -> np.ndarray:
        """Convert to flat array [Cx_12, Cx_13, ..., Cy_31, Cy_32]."""
        return np.array([
            self.Cx_12, self.Cx_13, self.Cx_21, self.Cx_23, self.Cx_31, self.Cx_32,
            self.Cy_12, self.Cy_13, self.Cy_21, self.Cy_23, self.Cy_31, self.Cy_32
        ])

    @classmethod
    def from_array(cls, arr: np.ndarray) -> "CouplingCoefficients":
        """Create from flat array."""
        return cls(
            Cx_12=arr[0], Cx_13=arr[1], Cx_21=arr[2], Cx_23=arr[3], Cx_31=arr[4], Cx_32=arr[5],
            Cy_12=arr[6], Cy_13=arr[7], Cy_21=arr[8], Cy_23=arr[9], Cy_31=arr[10], Cy_32=arr[11]
        )

    @classmethod
    def zeros(cls) -> "CouplingCoefficients":
        """Create zero coupling (uncoupled submodels)."""
        return cls.from_array(np.zeros(12))


def supermodel_ode(
    t: float,
    state: np.ndarray,
    submodel_params: list[LotkaVolterraParams],
    coupling: CouplingCoefficients
) -> np.ndarray:
    """
    ODE right-hand side for the coupled supermodel.

    State layout: [x1, y1, x2, y2, x3, y3]
        where x_k = prey for submodel k, y_k = predator for submodel k

    Args:
        t: Current time
        state: [x1, y1, x2, y2, x3, y3]
        submodel_params: List of 3 LotkaVolterraParams
        coupling: Coupling coefficients

    Returns:
        [dx1/dt, dy1/dt, dx2/dt, dy2/dt, dx3/dt, dy3/dt]
    """
    # Extract states for each submodel
    x1, y1 = state[0], state[1]
    x2, y2 = state[2], state[3]
    x3, y3 = state[4], state[5]

    # Compute uncoupled dynamics for each submodel
    f1 = lotka_volterra(t, np.array([x1, y1]), submodel_params[0])
    f2 = lotka_volterra(t, np.array([x2, y2]), submodel_params[1])
    f3 = lotka_volterra(t, np.array([x3, y3]), submodel_params[2])

    # Add coupling terms
    # Submodel 1: receives from 2 and 3
    dx1 = f1[0] + coupling.Cx_12 * (x2 - x1) + coupling.Cx_13 * (x3 - x1)
    dy1 = f1[1] + coupling.Cy_12 * (y2 - y1) + coupling.Cy_13 * (y3 - y1)

    # Submodel 2: receives from 1 and 3
    dx2 = f2[0] + coupling.Cx_21 * (x1 - x2) + coupling.Cx_23 * (x3 - x2)
    dy2 = f2[1] + coupling.Cy_21 * (y1 - y2) + coupling.Cy_23 * (y3 - y2)

    # Submodel 3: receives from 1 and 2
    dx3 = f3[0] + coupling.Cx_31 * (x1 - x3) + coupling.Cx_32 * (x2 - x3)
    dy3 = f3[1] + coupling.Cy_31 * (y1 - y3) + coupling.Cy_32 * (y2 - y3)

    return np.array([dx1, dy1, dx2, dy2, dx3, dy3])


def solve_supermodel(
    submodel_params: list[LotkaVolterraParams],
    coupling: CouplingCoefficients,
    t_span: tuple[float, float],
    y0: np.ndarray,
    t_eval: np.ndarray | None = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Integrate the coupled supermodel.

    All submodels start from the same initial condition.

    Args:
        submodel_params: Parameters for each of 3 submodels
        coupling: Coupling coefficients
        t_span: (t_start, t_end)
        y0: Initial conditions [x0, y0] (same for all submodels)
        t_eval: Time points for output

    Returns:
        t: Time points
        y_consensus: Consensus output [prey_avg, predator_avg] shape (2, n_times)
        y_all: All submodel states shape (6, n_times)
    """
    # Initial state: all submodels start at same point
    state0 = np.array([y0[0], y0[1], y0[0], y0[1], y0[0], y0[1]])

    # Event to stop integration if solution blows up
    def blowup_event(t, state):
        max_val = np.max(np.abs(state))
        return 1e6 - max_val  # Stops when any value exceeds 1e6

    blowup_event.terminal = True
    blowup_event.direction = -1

    sol = solve_ivp(
        fun=lambda t, state: supermodel_ode(t, state, submodel_params, coupling),
        t_span=t_span,
        y0=state0,
        t_eval=t_eval,
        method='LSODA',  # Auto-switches between stiff and non-stiff
        events=blowup_event
    )

    # Handle case where solution didn't complete (blew up)
    if sol.y.shape[1] == 0:
        # Return inf values
        n_points = len(t_eval) if t_eval is not None else 100
        return t_eval if t_eval is not None else np.linspace(t_span[0], t_span[1], n_points), \
               np.full((2, n_points), np.inf), \
               np.full((6, n_points), np.inf)

    # Extract consensus (average of submodels)
    x1, y1, x2, y2, x3, y3 = sol.y
    x_consensus = (x1 + x2 + x3) / 3
    y_consensus = (y1 + y2 + y3) / 3

    y_consensus_arr = np.vstack([x_consensus, y_consensus])

    return sol.t, y_consensus_arr, sol.y


@dataclass
class Supermodel:
    """Container for a trained supermodel."""
    submodels: list[TrainedSurrogate]
    coupling: CouplingCoefficients
    training_budget: int
    total_budget: int  # Including pretraining

    def solve(
        self,
        t_span: tuple[float, float],
        y0: np.ndarray,
        t_eval: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray]:
        """
        Solve the supermodel and return consensus trajectory.

        Returns:
            t: Time points
            y: Consensus trajectory [prey, predator]
        """
        params_list = [s.params for s in self.submodels]
        t, y_consensus, _ = solve_supermodel(
            params_list, self.coupling, t_span, y0, t_eval
        )
        return t, y_consensus

    def solve_all(
        self,
        t_span: tuple[float, float],
        y0: np.ndarray,
        t_eval: np.ndarray | None = None
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Solve and return both consensus and individual submodel trajectories.

        Returns:
            t: Time points
            y_consensus: Consensus [prey, predator]
            y_all: All states [x1, y1, x2, y2, x3, y3]
        """
        params_list = [s.params for s in self.submodels]
        return solve_supermodel(params_list, self.coupling, t_span, y0, t_eval)
