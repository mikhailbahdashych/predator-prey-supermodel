# Predator-Prey Supermodeling

Supermodeling implementation for predator-prey (Lotka-Volterra) dynamical systems using Approximate Bayesian Computation (ABC) for data assimilation.

## Overview

This project implements a supermodeling approach that combines multiple partially-trained submodels into a coupled ensemble, demonstrating that the combined supermodel can achieve comparable or better prediction quality than a single fully-trained model while using the same computational budget.

### Key Concepts

- **Baseline Model**: Ground-truth Lotka-Volterra predator-prey system
- **Surrogate Model 1**: Single model trained with full computational budget via ABC
- **Submodels 2, 3, 4**: Three models trained with 1/4 budget each (different random seeds for diversity)
- **Supermodel**: Coupled ensemble of submodels with learned coupling coefficients

## Installation

Requires Python 3.12+ and [uv](https://github.com/astral-sh/uv) package manager.

```bash
uv sync
```

## Usage

Run the full pipeline:

```bash
uv run main.py
```

This executes:
1. Ground-truth data generation with noisy observations
2. Surrogate 1 training (10,000 ABC evaluations)
3. Submodels 2-4 pretraining (2,500 evaluations each)
4. Supermodel coupling coefficient optimization (2,500 evaluations)
5. Model evaluation and comparison
6. Visualization generation

Results are saved to the `outputs/` directory.

## Project Structure

```
main.py                              # Entry point - runs full pipeline
src/
  models/
    lotka_volterra.py                # Base Lotka-Volterra ODE model
    supermodel.py                    # Coupled supermodel implementation
  data_assimilation/
    abc.py                           # ABC rejection sampling
  training/
    surrogate1.py                    # Full training for Surrogate 1
    surrogates234.py                 # Partial pretraining for submodels
    supermodel_training.py           # Coupling coefficient learning
  evaluation/
    compare.py                       # Metrics and model comparison
  utils/
    data_generation.py               # Observation generation
    plotting.py                      # Visualization
outputs/                             # Generated plots (after running)
```

## Lotka-Volterra Model

The predator-prey dynamics are governed by:

```
dx/dt = ax - bxy    (prey growth - predation)
dy/dt = dxy - cy    (predator growth - death)
```

Ground-truth parameters:
- a = 1.0 (prey birth rate)
- b = 0.1 (predation rate)
- d = 0.075 (predator efficiency)
- c = 1.5 (predator death rate)

## Supermodel Coupling

The supermodel couples three submodels through diffusive coupling:

```
dx_k/dt = f_x(x_k, y_k, params_k) + sum_{j!=k} C^x_{kj}(x_j - x_k)
dy_k/dt = f_y(x_k, y_k, params_k) + sum_{j!=k} C^y_{kj}(y_j - y_k)
```

The consensus output is the average across submodels:
```
x_s = (x_1 + x_2 + x_3) / 3
y_s = (y_1 + y_2 + y_3) / 3
```

12 coupling coefficients are learned via ABC:
- 6 for prey (C^x_{12}, C^x_{13}, C^x_{21}, C^x_{23}, C^x_{31}, C^x_{32})
- 6 for predator (C^y_{12}, C^y_{13}, C^y_{21}, C^y_{23}, C^y_{31}, C^y_{32})

## Computational Budget

The implementation enforces equal budget constraint:

| Component | Budget (model evaluations) |
|-----------|---------------------------|
| Surrogate 1 | 10,000 |
| Submodel 2 pretraining | 2,500 |
| Submodel 3 pretraining | 2,500 |
| Submodel 4 pretraining | 2,500 |
| Supermodel coupling | 2,500 |
| **Total supermodel** | **10,000** |

## Output Plots

After running, the following visualizations are generated in `outputs/`:

- `phase_portrait.png` - Phase space trajectories (prey vs predator)
- `time_series.png` - Population dynamics over time
- `mse_comparison.png` - MSE comparison across models
- `parameter_comparison.png` - Estimated vs ground-truth parameters
- `budget_comparison.png` - Computational budget breakdown

## Dependencies

- numpy - Numerical computations
- scipy - ODE integration
- matplotlib - Plotting
