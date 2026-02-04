"""PMAC lookup table generation using inverse distance weighting (IDW).

This module generates 2D PMAC flux linkage lookup tables with d-axis current
on the x-axis and q-axis current on the y-axis using IDW interpolation.
"""

import numpy as np
import pandas as pd


def interpolate_idw(
    id_data: np.ndarray,
    iq_data: np.ndarray,
    psi_d_data: np.ndarray,
    psi_q_data: np.ndarray,
    id_target: float,
    iq_target: float,
    max_dist: float,
) -> tuple:
    """Perform inverse distance weighting (IDW) interpolation.

    Uses weighted average of nearby points with weights inversely proportional
    to distance. Similar to the calculate() function in the VB macro approach.

    Args:
        id_data: Array of measured d-axis currents.
        iq_data: Array of measured q-axis currents.
        psi_d_data: Array of measured d-axis flux linkages.
        psi_q_data: Array of measured q-axis flux linkages.
        id_target: Target d-axis current point for interpolation.
        iq_target: Target q-axis current point for interpolation.
        max_dist: Maximum distance threshold for including points.

    Returns:
        Tuple containing interpolated (psi_d, psi_q) values.
    """
    # Calculate distances from target point to all data points
    distances = np.sqrt((id_data - id_target) ** 2 + (iq_data - iq_target) ** 2)

    # Find points within max distance threshold
    within_threshold = distances < max_dist

    # If no points within threshold, use nearest point
    if not np.any(within_threshold):
        nearest_idx = np.argmin(distances)
        return psi_d_data[nearest_idx], psi_q_data[nearest_idx]

    # Get distances and values for points within threshold
    dists_filtered = distances[within_threshold]
    psi_d_filtered = psi_d_data[within_threshold]
    psi_q_filtered = psi_q_data[within_threshold]

    # Apply inverse distance weighting
    # Protect against division by zero (exact match)
    dists_filtered = np.where(dists_filtered < 0.001, 0.001, dists_filtered)

    weights = 1.0 / dists_filtered
    weight_sum = np.sum(weights)

    # Calculate weighted average
    psi_d = np.sum(psi_d_filtered * weights) / weight_sum
    psi_q = np.sum(psi_q_filtered * weights) / weight_sum

    return psi_d, psi_q


def generate_pmac_tables(
    processed_data: pd.DataFrame, motor_params: dict, table_params: dict
) -> dict:
    """Generate 2D PMAC flux linkage lookup tables using IDW interpolation.

    Generates two 2D lookup tables for flux linkages (psi_d and psi_q)
    with d-axis current (Id) on the x-axis and q-axis current (Iq)
    on the y-axis using inverse distance weighting interpolation.

    Args:
        processed_data: DataFrame containing processed motor data with flux
                       linkage values (fluxLinkageDAxisWb,
                       fluxLinkageQAxisWb, currentDAxisApeak,
                       currentQAxisApeak).
        motor_params: Dictionary containing motor parameters (polePairs,
                     statorResistance).
        table_params: Dictionary containing table generation parameters
                     (size - grid resolution, maxCurrent - maximum current).

    Returns:
        Dictionary containing:
            - psi_d: 2D matrix of d-axis flux linkage (rows: Iq, cols: Id)
            - psi_q: 2D matrix of q-axis flux linkage (rows: Iq, cols: Id)
            - id_grid: Vector of d-axis current values (x-axis)
            - iq_grid: Vector of q-axis current values (y-axis)
            - id_matrix: 2D matrix of Id values
            - iq_matrix: 2D matrix of Iq values

    Example:
        table_params = {'size': 21, 'maxCurrent': 100}
        table_data = generate_pmac_tables(processed_data, motor_params,
                                        table_params)
    """
    # Validate inputs
    assert isinstance(table_params["size"], int), "Table size must be integer"
    assert table_params["size"] > 0, "Table size must be positive"
    assert table_params["maxCurrent"] > 0, "Max current must be positive"

    # Create current grids (matching VB macro behavior)
    # Id: from 0 to -maxCurrent (negative/decreasing)
    # Iq: from 0 to +maxCurrent (positive/increasing)
    size = table_params["size"]
    max_current = table_params["maxCurrent"]
    step = max_current / (size - 1)

    id_grid = np.linspace(0, -max_current, size)
    iq_grid = np.linspace(0, max_current, size)

    # Extract measurement data (convert DataFrame columns to arrays)
    id_data = processed_data["currentDAxisApeak"].values
    iq_data = processed_data["currentQAxisApeak"].values
    psi_d_data = processed_data["fluxLinkageDAxisWb"].values
    psi_q_data = processed_data["fluxLinkageQAxisWb"].values

    # Calculate maximum distance for IDW interpolation
    # Use a reasonable radius based on data spread
    id_data_range = np.max(id_data) - np.min(id_data)
    iq_data_range = np.max(iq_data) - np.min(iq_data)
    max_dist = np.sqrt(id_data_range**2 + iq_data_range**2) / 2

    print(f"IDW Max Distance Threshold: {max_dist:.4f} A")

    # Initialize output tables
    psi_d_table = np.zeros((size, size))
    psi_q_table = np.zeros((size, size))

    # Perform IDW interpolation
    # Loop through each grid point (matching VB macro loop structure)
    for x in range(size):
        id_target = id_grid[x]

        for y in range(size):
            iq_target = iq_grid[y]

            # Calculate IDW interpolation for this point
            psi_d, psi_q = interpolate_idw(
                id_data,
                iq_data,
                psi_d_data,
                psi_q_data,
                id_target,
                iq_target,
                max_dist,
            )

            psi_d_table[y, x] = psi_d
            psi_q_table[y, x] = psi_q

        # Progress indicator
        if (x + 1) % max(1, round(size / 10)) == 0:
            progress = 100 * (x + 1) / size
            print(f"  Progress: {progress:.0f}%")

    # Create mesh grids
    id_matrix, iq_matrix = np.meshgrid(id_grid, iq_grid)

    # Display summary
    print("===== PMAC Tables Generated (IDW Interpolation) =====")
    print(f"Table Size: {size}x{size}")
    print(f"Id Range: 0 to -{max_current} A")
    print(f"Iq Range: 0 to +{max_current} A")
    print(f"Current Step: {step:.6f} A")
    print(f"Psi_d Range: [{np.min(psi_d_table):.4f}, {np.max(psi_d_table):.4f}] Wb")
    print(f"Psi_q Range: [{np.min(psi_q_table):.4f}, {np.max(psi_q_table):.4f}] Wb")
    print("======================================================")

    return {
        "psi_d": psi_d_table,
        "psi_q": psi_q_table,
        "id_grid": id_grid,
        "iq_grid": iq_grid,
        "id_matrix": id_matrix,
        "iq_matrix": iq_matrix,
    }
