"""Main entry point for the motor flux map generation tool.

This script orchestrates the complete motor analysis workflow, focusing on
generating 2D flux linkage maps from processed measurement data.
"""

import sys

from src.config_loader import load_config
from src.data_loader import load_test_data
from src.data_processor import process_data
from src.motor_parameters import get_motor_parameters
from src.table_generator import generate_flux_maps
from src.table_parameters import get_table_parameters
from src.ui import plot_results


def main() -> None:
    """Execute the main flux map generation workflow.

    Orchestrates the complete process:
    0. Load configuration
    1. Load and validate test data
    2. Get motor parameters from user input
    3. Process raw data and calculate electrical parameters
    4a. Get table generation parameters from user input
    4b. Generate 2D flux linkage maps using generic interpolation
    5. Plot results (Interactive Dashboard)

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
            msg = "Failed to load data. Please check the file and try again."
            raise RuntimeError(msg)
        print()

        # Step 3: Get motor parameters
        print("Step 2: Getting motor parameters...")
        motor_params = get_motor_parameters(config)
        print()

        # Step 4: Process data
        print("Step 3: Processing data...")
        processed_data = process_data(data_table, motor_params, config)
        print()

        # Step 5: Get table parameters
        print("Step 4a: Getting table parameters...")
        table_params = get_table_parameters(config)
        print()

        # Step 6: Generate flux maps
        print("Step 4b: Generating flux maps...")
        generate_flux_maps(processed_data, motor_params, table_params, config)
        print()

        # Step 7: Plot results
        print("Step 5: Plotting results...")
        plot_results(processed_data, config)

        print("Analysis completed successfully!")

    except Exception as e:  # noqa: BLE001
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
