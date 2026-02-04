"""Data processing module for motor analysis.

This module provides functions for processing raw motor data and calculating
additional electrical parameters including flux linkages and electromagnetic torque.
"""

import pandas as pd

from src.lib.calculations.flux import (
    flux_linkage_d_voltage,
    flux_linkage_q_voltage,
)
from src.lib.calculations.frequency import electrical_frequency
from src.lib.calculations.torque import torque_flux


def peak_to_rms(peak_value: float) -> float:
    """Convert peak value to RMS value.

    Converts a peak value to its RMS equivalent using the standard
    relationship for sinusoidal waveforms.

    Args:
        peak_value: Peak value of the signal.

    Returns:
        RMS value (peak_value / sqrt(2))

    Formula:
        RMS = Peak / √2
    """
    import math

    return peak_value / math.sqrt(2)


def process_data(raw_data: pd.DataFrame, motor_params: dict) -> pd.DataFrame:
    """Process raw motor data and calculate additional parameters.

    Takes raw data table and motor parameters, processes the data,
    and calculates additional electrical parameters including flux linkages
    and electromagnetic torque.

    Args:
        raw_data: DataFrame containing raw measurement data with time, speed,
                 torque, voltage, and current measurements.
        motor_params: Dictionary containing motor parameters including
                     polePairs and statorResistance.

    Returns:
        Processed DataFrame with additional calculated columns including:
            - electricalFrequencyRads: Electrical frequency in rad/s
            - fluxLinkageDAxisWb: D-axis flux linkage in Weber-turns
            - fluxLinkageQAxisWb: Q-axis flux linkage in Weber-turns
            - torqueElectromagneticNm: Electromagnetic torque in Nm
            - currentDAxisArms: D-axis current RMS in Amperes
            - currentQAxisArms: Q-axis current RMS in Amperes
            - voltageDAxisVrms: D-axis voltage RMS in Volts
            - voltageQAxisVrms: Q-axis voltage RMS in Volts

    Example:
        motor_params = {'actual': {'polePairs': 4, 'statorResistance': 0.1}}
        processed_data = process_data(raw_data, motor_params)
    """
    processed_data = raw_data.copy()

    pole_pairs = motor_params["actual"]["polePairs"]
    stator_resistance = motor_params["actual"]["statorResistance"]

    # Calculate electrical frequency
    processed_data["electricalFrequencyRads"] = processed_data["speedRpm"].apply(
        lambda speed: electrical_frequency(speed, pole_pairs)
    )

    # Calculate flux linkages using voltage equation
    processed_data["fluxLinkageDAxisWb"] = processed_data.apply(
        lambda row: flux_linkage_d_voltage(
            row["voltageQAxisVpeak"],
            row["currentQAxisApeak"],
            row["electricalFrequencyRads"],
            stator_resistance,
        ),
        axis=1,
    )

    processed_data["fluxLinkageQAxisWb"] = processed_data.apply(
        lambda row: flux_linkage_q_voltage(
            row["voltageDAxisVpeak"],
            row["currentDAxisApeak"],
            row["electricalFrequencyRads"],
            stator_resistance,
        ),
        axis=1,
    )

    # Calculate electromagnetic torque using flux linkage and current
    processed_data["torqueElectromagneticNm"] = processed_data.apply(
        lambda row: torque_flux(
            row["fluxLinkageDAxisWb"],
            row["fluxLinkageQAxisWb"],
            row["currentQAxisApeak"],
            row["currentDAxisApeak"],
            pole_pairs,
        ),
        axis=1,
    )

    # Calculate RMS values from peak values
    processed_data["currentDAxisArms"] = processed_data["currentDAxisApeak"].apply(
        peak_to_rms
    )
    processed_data["currentQAxisArms"] = processed_data["currentQAxisApeak"].apply(
        peak_to_rms
    )
    processed_data["voltageDAxisVrms"] = processed_data["voltageDAxisVpeak"].apply(
        peak_to_rms
    )
    processed_data["voltageQAxisVrms"] = processed_data["voltageQAxisVpeak"].apply(
        peak_to_rms
    )

    # Display first few rows of processed data
    print("Processed data head:")
    print(processed_data.head())

    return processed_data
