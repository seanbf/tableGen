"""Main coordinator for motor parameter table generation.

This module coordinates the generation of various motor parameter lookup
tables (flux maps, etc.) by leveraging generic interpolation utilities
from the library.
"""

import numpy as np
import pandas as pd

from src.lib.utils import generate_2d_table, print_progress_indicator


def generate_flux_maps(
    processed_data: pd.DataFrame,
    motor_params: dict,
    table_params: dict,
    data_config: dict,
) -> dict:
    """Generate 2D flux linkage maps using generic IDW interpolation.

    This function coordinates the flux map generation process: preparing the
    data, defining the grid resolution, and calling the generic table
    generation engine from the library.

    Args:
        processed_data: DataFrame containing calculated motor parameters.
        motor_params: Dictionary containing pole pairs and stator resistance.
        table_params: Dictionary containing grid size and current range.
        data_config: Dictionary containing column name mappings.

    Returns:
        Dictionary containing d-axis and q-axis flux tables and their grids.
    """
    input_cols = data_config["data"]["standard_names"]["input"]
    comp_cols = data_config["data"]["standard_names"]["computed"]

    # Validate inputs
    assert isinstance(table_params["size"], int), "Table size must be integer"
    assert table_params["size"] > 0, "Table size must be positive"
    assert table_params["max_current_a"] > 0, "Max current must be positive"

    size = table_params["size"]
    max_current = table_params["max_current_a"]

    # Create current grids
    id_grid = np.linspace(0, -max_current, size)
    iq_grid = np.linspace(0, max_current, size)

    # Prepare data for generic interpolation
    coords = processed_data[[input_cols["id_apk"], input_cols["iq_apk"]]].values
    values = processed_data[
        [comp_cols["psi_d_wb"], comp_cols["psi_q_wb"]]
    ].values

    # Calculate maximum distance for IDW interpolation
    id_data_range = np.max(coords[:, 0]) - np.min(coords[:, 0])
    iq_data_range = np.max(coords[:, 1]) - np.min(coords[:, 1])
    max_dist = np.sqrt(id_data_range**2 + iq_data_range**2) / 2

    print(f"IDW Max Distance Threshold: {max_dist:.4f} A")

    # Use generic table generation engine from lib
    flux_maps = generate_2d_table(
        coords,
        values,
        id_grid,
        iq_grid,
        max_dist,
        progress_callback=print_progress_indicator
    )

    # Extract individual tables
    psi_d_table = flux_maps[:, :, 0]
    psi_q_table = flux_maps[:, :, 1]

    # Create mesh grids
    id_matrix, iq_matrix = np.meshgrid(id_grid, iq_grid)

    return {
        "psi_d": psi_d_table,
        "psi_q": psi_q_table,
        "id_grid": id_grid,
        "iq_grid": iq_grid,
        "id_matrix": id_matrix,
        "iq_matrix": iq_matrix,
    }
