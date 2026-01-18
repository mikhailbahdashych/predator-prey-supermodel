"""
Predator-Prey Supermodeling with ABC Data Assimilation

This script runs the full pipeline:
1. Generate ground-truth data and observations
2. Train Surrogate 1 with full budget
3. Train Submodels 2, 3, 4 with partial budgets
4. Train Supermodel coupling coefficients
5. Evaluate and compare all models
6. Generate visualizations

Time Budget Constraint:
- Surrogate 1: 10,000 evaluations
- Supermodel total: 7,500 (pretraining) + 2,500 (coupling) = 10,000 evaluations
"""

import numpy as np
from pathlib import Path

from src.utils.data_generation import generate_experiment_data
from src.training.surrogate1 import train_surrogate1
from src.training.surrogates234 import train_submodels
from src.training.supermodel_training import train_supermodel_coupling
from src.evaluation.compare import compare_models
from src.utils.plotting import generate_all_plots, export_all_csv


def main():
    """Run the full supermodeling pipeline."""
    print("=" * 70)
    print("PREDATOR-PREY SUPERMODELING WITH ABC DATA ASSIMILATION")
    print("=" * 70)

    # Configuration
    SEED = 42
    np.random.seed(SEED)

    # Time intervals
    T_TRAIN = (0.0, 15.0)   # Training interval
    T_TEST = (15.0, 25.0)   # Test/prediction interval

    # Initial conditions
    Y0 = np.array([10.0, 5.0])  # [prey, predator]

    # Budget configuration
    SURROGATE1_BUDGET = 10000
    SUBMODEL_BUDGET = 2500  # Per submodel
    N_SUBMODELS = 3
    COUPLING_BUDGET = SURROGATE1_BUDGET - (N_SUBMODELS * SUBMODEL_BUDGET)  # = 2500

    # Number of observations (2-3x number of parameters)
    N_OBSERVATIONS = 10

    print(f"\nConfiguration:")
    print(f"  Training interval: {T_TRAIN}")
    print(f"  Test interval: {T_TEST}")
    print(f"  Initial conditions: prey={Y0[0]}, predator={Y0[1]}")
    print(f"  Observations: {N_OBSERVATIONS}")
    print(f"  Surrogate 1 budget: {SURROGATE1_BUDGET}")
    print(f"  Submodel budget (each): {SUBMODEL_BUDGET}")
    print(f"  Coupling budget: {COUPLING_BUDGET}")

    # Step 1: Generate data
    print("\n" + "-" * 70)
    print("STEP 1: Generating ground-truth data and observations")
    print("-" * 70)

    train_truth, test_truth, observations = generate_experiment_data(
        y0=Y0,
        t_train=T_TRAIN,
        t_test=T_TEST,
        n_observations=N_OBSERVATIONS,
        noise_std=0.1,
        seed=SEED
    )

    print(f"  Training trajectory: {len(train_truth.t)} points")
    print(f"  Test trajectory: {len(test_truth.t)} points")
    print(f"  Observations: {len(observations)} points")
    print(f"  Observation times: {observations.t.round(2)}")

    # Step 2: Train Surrogate 1
    print("\n" + "-" * 70)
    print("STEP 2: Training Surrogate 1 (full budget)")
    print("-" * 70)

    surrogate1 = train_surrogate1(
        observations=observations,
        y0=Y0,
        t_span=T_TRAIN,
        budget=SURROGATE1_BUDGET,
        seed=SEED + 1,
        verbose=True
    )

    # Step 3: Train submodels
    print("\n" + "-" * 70)
    print("STEP 3: Training Submodels 2, 3, 4 (partial budgets)")
    print("-" * 70)

    submodels_result = train_submodels(
        observations=observations,
        y0=Y0,
        t_span=T_TRAIN,
        n_submodels=N_SUBMODELS,
        budget_per_submodel=SUBMODEL_BUDGET,
        base_seed=100,
        verbose=True
    )

    # Step 4: Train supermodel coupling
    print("\n" + "-" * 70)
    print("STEP 4: Training Supermodel coupling coefficients")
    print("-" * 70)

    supermodel = train_supermodel_coupling(
        submodels=submodels_result.submodels,
        observations=observations,
        y0=Y0,
        t_span=T_TRAIN,
        pretraining_budget=submodels_result.total_budget_used,
        budget=COUPLING_BUDGET,
        c_range=1.0,
        seed=200,
        verbose=True
    )

    # Step 5: Evaluate and compare
    print("\n" + "-" * 70)
    print("STEP 5: Evaluating and comparing models")
    print("-" * 70)

    results = compare_models(
        surrogate1=surrogate1,
        submodels=submodels_result.submodels,
        supermodel=supermodel,
        train_truth=train_truth,
        test_truth=test_truth,
        y0=Y0
    )

    results.print_summary()

    # Budget verification
    print("\n" + "-" * 70)
    print("BUDGET VERIFICATION")
    print("-" * 70)
    print(f"  Surrogate 1 budget: {surrogate1.abc_result.n_evaluations}")
    print(f"  Submodel pretraining: {submodels_result.total_budget_used}")
    print(f"  Coupling training: {supermodel.training_budget}")
    print(f"  Supermodel total: {supermodel.total_budget}")
    print(f"  Budget constraint (<= {SURROGATE1_BUDGET}): {'SATISFIED' if supermodel.total_budget <= SURROGATE1_BUDGET else 'VIOLATED'}")

    # Step 6: Generate visualizations
    print("\n" + "-" * 70)
    print("STEP 6: Generating visualizations")
    print("-" * 70)

    output_dir = Path("outputs")
    generate_all_plots(
        train_truth=train_truth,
        test_truth=test_truth,
        observations=observations,
        surrogate1=surrogate1,
        submodels=submodels_result.submodels,
        supermodel=supermodel,
        results=results,
        y0=Y0,
        output_dir=output_dir
    )

    export_all_csv(
        train_truth=train_truth,
        test_truth=test_truth,
        observations=observations,
        surrogate1=surrogate1,
        submodels=submodels_result.submodels,
        supermodel=supermodel,
        results=results,
        y0=Y0,
        output_dir=output_dir
    )

    print("\n" + "=" * 70)
    print("PIPELINE COMPLETE")
    print("=" * 70)
    print(f"\nOutputs saved to: {output_dir.absolute()}")
    print("\nGenerated files:")
    print("  Plots:")
    for f in sorted(output_dir.glob("*.png")):
        print(f"    - {f.name}")
    print("  Data:")
    for f in sorted(output_dir.glob("*.csv")):
        print(f"    - {f.name}")


if __name__ == "__main__":
    main()
