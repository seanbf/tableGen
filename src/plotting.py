"""Plotting module for motor analysis results.

This module provides functions for creating visualizations of motor analysis
data including torque comparison plots.
"""

import matplotlib.pyplot as plt


def plot_results(data) -> None:
    """Plot torque comparison results.

    Creates a line plot comparing electromagnetic torque and measured torque
    over time using standard electrical engineering notation.

    Args:
        data: DataFrame containing processed data with timeS,
             torqueElectromagneticNm, torqueMeasuredNm, and other
             electrical parameters.

    Raises:
        ValueError: If required columns are missing from the data.

    Example:
        plot_results(processed_data)
    """
    # Check if required columns exist
    required_columns = [
        "timeS",
        "torqueElectromagneticNm",
        "torqueMeasuredNm",
    ]

    missing_columns = [
        col for col in required_columns if col not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Required columns {missing_columns} not found in data"
        )

    # Create figure and plot
    plt.figure()
    plt.plot(
        data["timeS"],
        data["torqueElectromagneticNm"],
        "b-",
        label="Torque Electromagnetic",
    )
    plt.plot(
        data["timeS"],
        data["torqueMeasuredNm"],
        "r--",
        label="Torque Measured",
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Torque (Nm)")
    plt.title("Torque Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()
