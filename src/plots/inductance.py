"""Inductance mapping visualization.

This module provides functions to create 3D surface traces for inductance
maps, interpolating calculated data for visualization.
"""

import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata


def generate_inductance_surface(
    current_d: np.ndarray,
    current_q: np.ndarray,
    inductance_values: np.ndarray,
    name: str,
    colorbar_config: dict = None,
) -> go.Surface:
    """Create a 3D Surface trace for inductance.

    Interpolates scattered (Id, Iq, L) data onto a regular grid and returns
    a Plotly Surface trace. Uses 'Plasma' colormap to distinguish from flux.

    Args:
        current_d: Array of D-axis current points (x).
        current_q: Array of Q-axis current points (y).
        inductance_values: Array of Inductance values (z).
        name: Name of the trace (e.g., "Ld").
        colorbar_config: Optional dictionary for colorbar customization.

    Returns:
        go.Surface: Interactive 3D surface trace.
    """
    if colorbar_config is None:
        colorbar_config = {}

    # Filter out NaNs and infinities which can happen with zero current division
    valid_mask = np.isfinite(inductance_values)
    cd = current_d[valid_mask]
    cq = current_q[valid_mask]
    lv = inductance_values[valid_mask]

    if len(cd) < 4:  # Need enough points for interpolation
        return go.Surface(name=name)

    # Create grid for interpolation
    grid_res = 100
    grid_id, grid_iq = np.mgrid[
        min(cd) : max(cd) : complex(grid_res),
        min(cq) : max(cq) : complex(grid_res),
    ]

    try:
        grid_l = griddata(
            (cd, cq), lv, (grid_id, grid_iq), method="cubic"
        )
    except Exception as e:
        print(f"Interpolation failed for {name}: {e}")
        grid_l = np.zeros_like(grid_id)

    # Create Surface Trace
    return go.Surface(
        x=grid_id,
        y=grid_iq,
        z=grid_l,
        colorscale="Plasma",
        name=name,
        colorbar=colorbar_config,
        contours_z=dict(show=True, usecolormap=True, project_z=True),
        hovertemplate=(
            "Id: %{x:.2f} A<br>Iq: %{y:.2f} A<br>L: %{z:.6f} H<extra></extra>"
        ),
    )
