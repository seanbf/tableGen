"""Data loading and validation module for motor analysis.

This module provides functions for loading CSV test data and validating
that required columns are present in the loaded data.
"""

from pathlib import Path
from typing import Tuple

import pandas as pd


def load_test_data(
    data_config: dict, relative_path: str = "sample_data/sample.csv"
) -> Tuple[pd.DataFrame, bool]:
    """Load and validate CSV data for motor analysis.

    Loads a CSV file and renames columns according to standard electrical
    engineering notation. Returns the loaded table and a success flag.

    Args:
        data_config: Dictionary containing column name mappings and standard names.
        relative_path: Relative path to the CSV file from project root.

    Returns:
        Tuple containing:
            - DataFrame with loaded and renamed data
            - Boolean indicating if loading was successful

    Example:
        data_table, success = load_test_data(data_config)
        if success:
            print("Data loaded successfully")
    """
    success_flag = False
    data_table = None

    # Get project root
    project_root = Path(__file__).parent.parent
    full_path = project_root / relative_path

    # Read CSV file
    try:
        data_table = pd.read_csv(full_path)
        print(f"Successfully loaded: {full_path.name}")
        print(f"Data size: {data_table.shape[0]} rows x {data_table.shape[1]} columns")
        success_flag = True
    except FileNotFoundError:
        print(f"Error: File not found at {full_path}")
        return data_table, success_flag
    except Exception as e:  # noqa: BLE001
        print(f"Error reading file: {e}")
        return data_table, success_flag

    # Extract column name mappings
    col = data_config["data"]["columnNames"]
    std_names = data_config["data"]["standardNames"]

    # Select only relevant columns
    selected_cols = [
        col["time"],
        col["torqueMeasured"],
        col["speedMeasured"],
        col["voltageQAxis"],
        col["voltageDAxis"],
        col["currentQAxis"],
        col["currentDAxis"],
    ]

    try:
        data_table = data_table[selected_cols]

        # Rename columns with descriptive names using standard notation
        rename_mapping = {
            col["time"]: std_names["time"],
            col["speedMeasured"]: std_names["speedMeasured"],
            col["torqueMeasured"]: std_names["torqueMeasured"],
            col["voltageQAxis"]: std_names["voltageQAxis"],
            col["voltageDAxis"]: std_names["voltageDAxis"],
            col["currentQAxis"]: std_names["currentQAxis"],
            col["currentDAxis"]: std_names["currentDAxis"],
        }

        data_table = data_table.rename(columns=rename_mapping)
        print("Selected and renamed relevant columns successfully")

    except KeyError as e:
        print(f"Error selecting columns: {e}")
        data_table = None
        success_flag = False
        return data_table, success_flag

    return data_table, success_flag
