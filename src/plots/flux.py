"""Flux mapping module.

This module provides a reusable function to create 3D Surface traces for flux
linkage maps, including IDW/Griddata interpolation.
"""

import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata


def generate_flux_surface(
    current_d: np.ndarray,
    current_q: np.ndarray,
    flux_values: np.ndarray,
    name: str,
    colorbar_config: dict = None,
) -> go.Surface:
    """Create a 3D Surface trace for flux linkage.

    Interpolates scattered (Id, Iq, Flux) data onto a regular grid and returns
    a Plotly Surface trace. Uses 'Viridis' colormap.

    Args:
        current_d: Array of D-axis current points (x).
        current_q: Array of Q-axis current points (y).
        flux_values: Array of Flux values (z).
        name: Name of the trace (e.g., "Flux D").
        colorbar_config: Optional dictionary for colorbar customization.

    Returns:
        go.Surface: Interactive 3D surface trace.
    """
    if colorbar_config is None:
        colorbar_config = {}

    # Create grid for interpolation
    grid_res = 100
    grid_id, grid_iq = np.mgrid[
        min(current_d) : max(current_d) : complex(grid_res),
        min(current_q) : max(current_q) : complex(grid_res),
    ]

    try:
        grid_flux = griddata(
            (current_d, current_q), flux_values, (grid_id, grid_iq), method="cubic"
        )
    except Exception as e:
        print(f"Interpolation failed for {name}: {e}")
        grid_flux = np.zeros_like(grid_id)

    # Create Surface Trace
    return go.Surface(
        x=grid_id,
        y=grid_iq,
        z=grid_flux,
        colorscale="Viridis",
        name=name,
        colorbar=colorbar_config,
        contours_z=dict(show=True, usecolormap=True, project_z=True),
        hovertemplate="Id: %{x:.2f} A<br>Iq: %{y:.2f} A<br>Flux: %{z:.4f} Wb<extra></extra>",
    )
