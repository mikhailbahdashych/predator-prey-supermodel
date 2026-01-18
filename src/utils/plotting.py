"""
Plotting Utilities for Predator-Prey Supermodeling

Generates visualizations for model comparison.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from src.models.lotka_volterra import (
    LotkaVolterraParams,
    solve_lotka_volterra,
    GROUND_TRUTH_PARAMS
)
from src.models.supermodel import Supermodel
from src.training.surrogate1 import TrainedSurrogate
from src.utils.data_generation import TrajectoryData, Observations
from src.evaluation.compare import ComparisonResults


def setup_style():
    """Setup matplotlib style for consistent plots."""
    plt.rcParams.update({
        'figure.figsize': (12, 8),
        'font.size': 11,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'legend.fontsize': 10,
        'lines.linewidth': 2,
        'axes.grid': True,
        'grid.alpha': 0.3
    })


def plot_phase_portrait(
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    surrogate1: TrainedSurrogate,
    supermodel: Supermodel,
    observations: Observations,
    y0: np.ndarray,
    output_path: Path
):
    """
    Plot phase portrait (prey vs predator) for all models.

    Args:
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        surrogate1: Trained surrogate model
        supermodel: Trained supermodel
        observations: Training observations
        y0: Initial conditions
        output_path: Path to save plot
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 8))

    # Full ground truth trajectory
    full_t = np.concatenate([train_truth.t, test_truth.t])
    full_prey = np.concatenate([train_truth.prey, test_truth.prey])
    full_pred = np.concatenate([train_truth.predator, test_truth.predator])

    ax.plot(full_prey, full_pred, 'k-', linewidth=2.5, label='Ground Truth', alpha=0.8)

    # Surrogate 1
    t_span = (train_truth.t[0], test_truth.t[-1])
    t_eval = np.linspace(t_span[0], t_span[1], 400)
    _, y_surr1 = solve_lotka_volterra(surrogate1.params, t_span, y0, t_eval)
    ax.plot(y_surr1[0], y_surr1[1], 'b--', linewidth=2, label='Surrogate 1 (Full Training)', alpha=0.8)

    # Supermodel (use returned t values since they may differ due to early termination)
    t_super, y_super = supermodel.solve(t_span, y0, t_eval)
    ax.plot(y_super[0], y_super[1], 'r-', linewidth=2, label='Supermodel (Coupled)', alpha=0.8)

    # Observations
    ax.scatter(observations.prey, observations.predator, c='green', s=100,
               marker='o', label='Observations', zorder=5, edgecolors='black')

    # Mark training/test boundary
    boundary_idx = len(train_truth.t) - 1
    ax.scatter([train_truth.prey[-1]], [train_truth.predator[-1]],
               c='orange', s=150, marker='*', label='Train/Test Boundary',
               zorder=6, edgecolors='black')

    ax.set_xlabel('Prey Population (x)')
    ax.set_ylabel('Predator Population (y)')
    ax.set_title('Phase Portrait: Predator-Prey Dynamics')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def plot_time_series(
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    surrogate1: TrainedSurrogate,
    supermodel: Supermodel,
    observations: Observations,
    y0: np.ndarray,
    output_path: Path
):
    """
    Plot time series of prey and predator populations.

    Args:
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        surrogate1: Trained surrogate model
        supermodel: Trained supermodel
        observations: Training observations
        y0: Initial conditions
        output_path: Path to save plot
    """
    setup_style()
    fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    t_span = (train_truth.t[0], test_truth.t[-1])
    t_eval = np.linspace(t_span[0], t_span[1], 400)

    # Full ground truth
    full_t = np.concatenate([train_truth.t, test_truth.t])
    full_prey = np.concatenate([train_truth.prey, test_truth.prey])
    full_pred = np.concatenate([train_truth.predator, test_truth.predator])

    # Surrogate 1
    _, y_surr1 = solve_lotka_volterra(surrogate1.params, t_span, y0, t_eval)

    # Supermodel (use returned t values since they may differ due to early termination)
    t_super, y_super = supermodel.solve(t_span, y0, t_eval)

    # Training/test boundary
    t_boundary = train_truth.t[-1]

    # --- Prey subplot ---
    ax = axes[0]
    ax.axvline(t_boundary, color='gray', linestyle=':', linewidth=2, alpha=0.7, label='Train/Test Boundary')
    ax.axvspan(t_boundary, test_truth.t[-1], alpha=0.1, color='gray')

    ax.plot(full_t, full_prey, 'k-', linewidth=2.5, label='Ground Truth')
    ax.plot(t_eval, y_surr1[0], 'b--', linewidth=2, label='Surrogate 1')
    ax.plot(t_super, y_super[0], 'r-', linewidth=2, label='Supermodel')
    ax.scatter(observations.t, observations.prey, c='green', s=80, marker='o',
               label='Observations', zorder=5, edgecolors='black')

    ax.set_ylabel('Prey Population (x)')
    ax.set_title('Time Series: Prey Population')
    ax.legend(loc='upper right')
    ax.text(t_boundary + 0.5, ax.get_ylim()[1] * 0.9, 'PREDICTION', fontsize=10, alpha=0.7)

    # --- Predator subplot ---
    ax = axes[1]
    ax.axvline(t_boundary, color='gray', linestyle=':', linewidth=2, alpha=0.7)
    ax.axvspan(t_boundary, test_truth.t[-1], alpha=0.1, color='gray')

    ax.plot(full_t, full_pred, 'k-', linewidth=2.5, label='Ground Truth')
    ax.plot(t_eval, y_surr1[1], 'b--', linewidth=2, label='Surrogate 1')
    ax.plot(t_super, y_super[1], 'r-', linewidth=2, label='Supermodel')
    ax.scatter(observations.t, observations.predator, c='green', s=80, marker='o',
               label='Observations', zorder=5, edgecolors='black')

    ax.set_xlabel('Time')
    ax.set_ylabel('Predator Population (y)')
    ax.set_title('Time Series: Predator Population')
    ax.legend(loc='upper right')
    ax.text(t_boundary + 0.5, ax.get_ylim()[1] * 0.9, 'PREDICTION', fontsize=10, alpha=0.7)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def plot_mse_comparison(
    results: ComparisonResults,
    output_path: Path
):
    """
    Plot MSE comparison bar chart.

    Args:
        results: Comparison results
        output_path: Path to save plot
    """
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Collect data (excluding baseline which is 0)
    models = [results.surrogate1] + results.submodels + [results.supermodel]
    names = [m.name.replace(' (', '\n(') for m in models]
    mse_train = [m.mse_train for m in models]
    mse_test = [m.mse_test for m in models]

    colors = ['blue'] + ['gray'] * len(results.submodels) + ['red']

    x = np.arange(len(names))
    width = 0.6

    # Training MSE
    ax = axes[0]
    bars = ax.bar(x, mse_train, width, color=colors, alpha=0.7, edgecolor='black')
    ax.set_ylabel('MSE')
    ax.set_title('Training Interval MSE')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=9)
    ax.set_yscale('log')

    # Test MSE
    ax = axes[1]
    bars = ax.bar(x, mse_test, width, color=colors, alpha=0.7, edgecolor='black')
    ax.set_ylabel('MSE')
    ax.set_title('Test/Prediction Interval MSE')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=9)
    ax.set_yscale('log')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def plot_parameter_comparison(
    surrogate1: TrainedSurrogate,
    submodels: list[TrainedSurrogate],
    output_path: Path
):
    """
    Plot parameter comparison across models.

    Args:
        surrogate1: Fully trained surrogate
        submodels: Partially trained submodels
        output_path: Path to save plot
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(12, 6))

    param_names = [r'$\alpha$ (prey birth)', r'$\beta$ (predation)',
                   r'$\delta$ (pred. efficiency)', r'$\gamma$ (pred. death)']

    # Ground truth
    gt = GROUND_TRUTH_PARAMS.to_array()

    # All models
    models = [('Ground Truth', gt, 'black'),
              ('Surrogate 1', surrogate1.params.to_array(), 'blue')]

    for i, s in enumerate(submodels):
        models.append((f'Submodel {i+2}', s.params.to_array(), f'C{i+2}'))

    x = np.arange(len(param_names))
    width = 0.15
    offsets = np.linspace(-width * (len(models) - 1) / 2, width * (len(models) - 1) / 2, len(models))

    for (name, params, color), offset in zip(models, offsets):
        ax.bar(x + offset, params, width, label=name, color=color, alpha=0.7, edgecolor='black')

    ax.set_ylabel('Parameter Value')
    ax.set_title('Parameter Comparison: Ground Truth vs Estimated')
    ax.set_xticks(x)
    ax.set_xticklabels(param_names)
    ax.legend(loc='upper right')
    ax.axhline(0, color='gray', linewidth=0.5)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def plot_budget_comparison(
    results: ComparisonResults,
    output_path: Path
):
    """
    Plot computational budget comparison.

    Args:
        results: Comparison results
        output_path: Path to save plot
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 6))

    # Budget data
    categories = ['Surrogate 1\n(Full Training)', 'Supermodel\n(Total)']
    budgets = [results.surrogate1.budget_used, results.supermodel.budget_used]

    # Supermodel breakdown
    pretraining = sum(s.budget_used for s in results.submodels)
    coupling = results.supermodel.budget_used - pretraining

    colors = ['blue', 'red']
    bars = ax.bar(categories, budgets, color=colors, alpha=0.7, edgecolor='black', width=0.5)

    # Add breakdown text on supermodel bar
    ax.text(1, pretraining / 2, f'Pretraining\n{pretraining}', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text(1, pretraining + coupling / 2, f'Coupling\n{coupling}', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    # Add exact values on top
    for bar, budget in zip(bars, budgets):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100,
                f'{budget:,}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_ylabel('Model Evaluations')
    ax.set_title('Computational Budget Comparison')
    ax.set_ylim(0, max(budgets) * 1.15)

    # Add constraint line
    constraint = results.surrogate1.budget_used
    ax.axhline(constraint, color='green', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(1.3, constraint, f'Budget Constraint: {constraint:,}', va='center', fontsize=10, color='green')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def generate_all_plots(
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    observations: Observations,
    surrogate1: TrainedSurrogate,
    submodels: list[TrainedSurrogate],
    supermodel: Supermodel,
    results: ComparisonResults,
    y0: np.ndarray,
    output_dir: Path
):
    """
    Generate all visualization plots.

    Args:
        train_truth: Ground truth training trajectory
        test_truth: Ground truth test trajectory
        observations: Training observations
        surrogate1: Fully trained surrogate
        submodels: Partially trained submodels
        supermodel: Trained supermodel
        results: Comparison results
        y0: Initial conditions
        output_dir: Directory to save plots
    """
    print("\nGenerating plots...")

    output_dir.mkdir(parents=True, exist_ok=True)

    plot_phase_portrait(
        train_truth, test_truth, surrogate1, supermodel, observations, y0,
        output_dir / "phase_portrait.png"
    )

    plot_time_series(
        train_truth, test_truth, surrogate1, supermodel, observations, y0,
        output_dir / "time_series.png"
    )

    plot_mse_comparison(
        results,
        output_dir / "mse_comparison.png"
    )

    plot_parameter_comparison(
        surrogate1, submodels,
        output_dir / "parameter_comparison.png"
    )

    plot_budget_comparison(
        results,
        output_dir / "budget_comparison.png"
    )

    print(f"\nAll plots saved to: {output_dir}")


def export_trajectories_csv(
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    surrogate1: TrainedSurrogate,
    supermodel: Supermodel,
    y0: np.ndarray,
    output_dir: Path
):
    """Export trajectory data to CSV files."""
    import csv

    # Ground truth trajectory
    full_t = np.concatenate([train_truth.t, test_truth.t])
    full_prey = np.concatenate([train_truth.prey, test_truth.prey])
    full_pred = np.concatenate([train_truth.predator, test_truth.predator])

    with open(output_dir / "ground_truth_trajectory.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'prey', 'predator'])
        for t, x, y in zip(full_t, full_prey, full_pred):
            writer.writerow([t, x, y])

    # Surrogate 1 trajectory
    t_span = (train_truth.t[0], test_truth.t[-1])
    t_eval = np.linspace(t_span[0], t_span[1], 400)
    _, y_surr1 = solve_lotka_volterra(surrogate1.params, t_span, y0, t_eval)

    with open(output_dir / "surrogate1_trajectory.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'prey', 'predator'])
        for t, x, y in zip(t_eval, y_surr1[0], y_surr1[1]):
            writer.writerow([t, x, y])

    # Supermodel trajectory
    t_super, y_super = supermodel.solve(t_span, y0, t_eval)

    with open(output_dir / "supermodel_trajectory.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'prey', 'predator'])
        for t, x, y in zip(t_super, y_super[0], y_super[1]):
            writer.writerow([t, x, y])

    print(f"  Saved: {output_dir}/ground_truth_trajectory.csv")
    print(f"  Saved: {output_dir}/surrogate1_trajectory.csv")
    print(f"  Saved: {output_dir}/supermodel_trajectory.csv")


def export_observations_csv(
    observations: Observations,
    output_dir: Path
):
    """Export observations to CSV."""
    import csv

    with open(output_dir / "observations.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'prey', 'predator'])
        for t, x, y in zip(observations.t, observations.prey, observations.predator):
            writer.writerow([t, x, y])

    print(f"  Saved: {output_dir}/observations.csv")


def export_model_comparison_csv(
    results: ComparisonResults,
    output_dir: Path
):
    """Export model comparison results to CSV."""
    import csv

    with open(output_dir / "model_comparison.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['model', 'mse_train', 'mse_test', 'rmse_train', 'rmse_test', 'budget_used'])

        for m in [results.baseline, results.surrogate1] + results.submodels + [results.supermodel]:
            writer.writerow([m.name, m.mse_train, m.mse_test, m.rmse_train, m.rmse_test, m.budget_used])

    print(f"  Saved: {output_dir}/model_comparison.csv")


def export_parameters_csv(
    surrogate1: TrainedSurrogate,
    submodels: list[TrainedSurrogate],
    supermodel: Supermodel,
    output_dir: Path
):
    """Export model parameters to CSV."""
    import csv

    # Lotka-Volterra parameters
    with open(output_dir / "model_parameters.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['model', 'alpha', 'beta', 'delta', 'gamma'])

        # Ground truth
        writer.writerow(['Ground Truth', 1.0, 0.1, 0.075, 1.5])

        # Surrogate 1
        p = surrogate1.params
        writer.writerow([surrogate1.name, p.alpha, p.beta, p.delta, p.gamma])

        # Submodels
        for s in submodels:
            p = s.params
            writer.writerow([s.name, p.alpha, p.beta, p.delta, p.gamma])

    # Coupling coefficients
    c = supermodel.coupling
    with open(output_dir / "coupling_coefficients.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['coefficient', 'value'])
        writer.writerow(['Cx_12', c.Cx_12])
        writer.writerow(['Cx_13', c.Cx_13])
        writer.writerow(['Cx_21', c.Cx_21])
        writer.writerow(['Cx_23', c.Cx_23])
        writer.writerow(['Cx_31', c.Cx_31])
        writer.writerow(['Cx_32', c.Cx_32])
        writer.writerow(['Cy_12', c.Cy_12])
        writer.writerow(['Cy_13', c.Cy_13])
        writer.writerow(['Cy_21', c.Cy_21])
        writer.writerow(['Cy_23', c.Cy_23])
        writer.writerow(['Cy_31', c.Cy_31])
        writer.writerow(['Cy_32', c.Cy_32])

    print(f"  Saved: {output_dir}/model_parameters.csv")
    print(f"  Saved: {output_dir}/coupling_coefficients.csv")


def export_all_csv(
    train_truth: TrajectoryData,
    test_truth: TrajectoryData,
    observations: Observations,
    surrogate1: TrainedSurrogate,
    submodels: list[TrainedSurrogate],
    supermodel: Supermodel,
    results: ComparisonResults,
    y0: np.ndarray,
    output_dir: Path
):
    """Export all data to CSV files."""
    print("\nExporting CSV data...")

    export_trajectories_csv(train_truth, test_truth, surrogate1, supermodel, y0, output_dir)
    export_observations_csv(observations, output_dir)
    export_model_comparison_csv(results, output_dir)
    export_parameters_csv(surrogate1, submodels, supermodel, output_dir)

    print(f"\nAll CSV files saved to: {output_dir}")
