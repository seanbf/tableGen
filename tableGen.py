"""Main entry point for PMAC table generation tool.

This script orchestrates the complete motor analysis workflow using modular
functions with standard electrical engineering unit notation and comprehensive
documentation.
"""

import sys
from pathlib import Path

from src.config_loader import load_config
from src.data_loader import load_test_data
from src.data_processor import process_data
from src.motor_parameters import get_motor_parameters
from src.plotting import plot_results
from src.table_generator import generate_pmac_tables
from src.table_parameters import get_table_parameters


def main() -> None:
    """Execute the main PMAC table generation workflow.

    Orchestrates the complete process:
    1. Load and validate test data
    2. Get motor parameters from user input
    3. Process raw data and calculate electrical parameters
    4. Get table generation parameters from user input
    5. Generate PMAC lookup tables using IDW interpolation
    6. Plot results

    Exits with status code 1 if any step fails.
    """
    try:
        # Step 1: Load configuration
        print("Step 0: Loading configuration...")
        config = load_config()
        print("Configuration loaded successfully\n")

        # Step 2: Load and validate data
        print("Step 1: Loading and validating data...")
        data_table, success_flag = load_test_data(config)

        if not success_flag:
            raise RuntimeError("Failed to load data. Please check the file and try again.")
        print()

        # Step 3: Get motor parameters
        print("Step 2: Getting motor parameters...")
        motor_params = get_motor_parameters(config)
        print()

        # Step 4: Process data
        print("Step 3: Processing data...")
        processed_data = process_data(data_table, motor_params)
        print()

        # Step 5: Get table parameters
        print("Step 4a: Getting table parameters...")
        table_params = get_table_parameters(config)
        print()

        # Step 6: Generate PMAC tables
        print("Step 4b: Generating PMAC tables...")
        table_data = generate_pmac_tables(processed_data, motor_params, table_params)
        print()

        # Step 7: Plot results
        print("Step 5: Plotting results...")
        plot_results(processed_data)

        print("Analysis completed successfully!")

    except Exception as e:  # noqa: BLE001
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
