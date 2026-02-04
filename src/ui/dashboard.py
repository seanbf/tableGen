"""Dashboard plotting module.

This module assembles the main dashboard using traces from sub-modules.
"""

import pandas as pd
from plotly.subplots import make_subplots

from src.plots.flux import generate_flux_surface
from src.plots.torque import get_torque_traces


def plot_results(data: pd.DataFrame, data_config: dict) -> None:
    """Plot motor analysis results dashboard.

    Creates a single interactive dashboard window containing torque comparison
    and flux linkage surfaces.

    Args:
        data: DataFrame containing processed data.
        data_config: Dictionary containing column name configurations.
    """
    input_cols = data_config["data"]["standardNames"]["input"]
    comp_cols = data_config["data"]["standardNames"]["computed"]

    # Validation
    required_columns = [
        input_cols["time"],
        comp_cols["torque_e_nm"],
        input_cols["torque_measured"],
        input_cols["id_apk"],
        input_cols["iq_apk"],
        comp_cols["psi_d_wb"],
        comp_cols["psi_q_wb"],
    ]
    missing = [c for c in required_columns if c not in data.columns]
    if missing:
        raise ValueError(f"Required columns {missing} not found in data")

    # Create subplot layout
    fig = make_subplots(
        rows=2,
        cols=2,
        specs=[
            [{"colspan": 2, "type": "xy"}, None],
            [{"type": "surface"}, {"type": "surface"}],
        ],
        subplot_titles=(
            "Torque Comparison",
            "Flux Linkage D-Axis",
            "Flux Linkage Q-Axis",
        ),
        vertical_spacing=0.1,
    )

    # Add Torque Traces
    torque_traces = get_torque_traces(data)
    for trace in torque_traces:
        fig.add_trace(trace, row=1, col=1)

    # --- Add Flux Traces ---
    id_points = data[input_cols["id_apk"]].values
    iq_points = data[input_cols["iq_apk"]].values

    # Flux D
    flux_d_trace = generate_flux_surface(
        current_d=id_points,
        current_q=iq_points,
        flux_values=data[comp_cols["psi_d_wb"]].values,
        name="Flux D",
        colorbar_config=dict(
            x=-0.07,  # Far left
            len=0.45,
            y=0,
            yanchor="bottom",
        ),
    )
    fig.add_trace(flux_d_trace, row=2, col=1)

    # Flux Q
    flux_q_trace = generate_flux_surface(
        current_d=id_points,
        current_q=iq_points,
        flux_values=data[comp_cols["psi_q_wb"]].values,
        name="Flux Q",
        colorbar_config=dict(len=0.45, y=0, yanchor="bottom"),
    )
    fig.add_trace(flux_q_trace, row=2, col=2)

    # Update Layout
    fig.update_layout(
        title="Motor Analysis Dashboard",
        height=900,
        template="plotly_white",
        showlegend=True,
        hovermode="x unified",
    )

    # Axis Titles
    fig.update_xaxes(title_text="Time (s)", row=1, col=1)
    fig.update_yaxes(title_text="Torque (Nm)", row=1, col=1)

    common_3d_axis = dict(
        xaxis_title="Id (A)", yaxis_title="Iq (A)", zaxis_title="Psi (Wb)"
    )
    fig.update_scenes(common_3d_axis, row=2, col=1)
    fig.update_scenes(common_3d_axis, row=2, col=2)

    fig.show()


# End of module
