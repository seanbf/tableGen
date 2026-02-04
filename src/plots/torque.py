"""Torque plotting module.

This module provides functions to create Plotly traces for torque comparison.
"""

import pandas as pd
import plotly.graph_objects as go


def get_torque_traces(data: pd.DataFrame) -> list[go.Scattergl]:
    """Create traces for torque comparison plot.

    Args:
        data: processed DataFrame

    Returns:
        List of plotly traces (Electromagnetic and Measured torque)
    """
    traces = []

    # Electromagnetic Torque
    traces.append(
        go.Scattergl(
            x=data["timeS"],
            y=data["torqueElectromagneticNm"],
            mode="lines",
            name="Torque Electromagnetic",
            # Standard colors
        )
    )

    # Measured Torque
    traces.append(
        go.Scattergl(
            x=data["timeS"],
            y=data["torqueMeasuredNm"],
            mode="lines",
            name="Torque Measured",
            # Standard colors
        )
    )

    return traces
