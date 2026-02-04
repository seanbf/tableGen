"""Data processing module for motor analysis.

This module provides functions for processing raw motor data and calculating
additional electrical parameters including flux linkages, inductances,
and electromagnetic torque.
"""

import pandas as pd

from src.lib.calculations.flux import (
    flux_linkage_d_voltage,
    flux_linkage_q_voltage,
)
from src.lib.calculations.frequency import electrical_frequency
from src.lib.calculations.inductance import (
    inductance_d,
    inductance_q,
)
from src.lib.calculations.torque import torque_flux
from src.lib.conversions.waveform import peak_to_rms


def process_data(
    raw_data: pd.DataFrame, motor_params: dict, data_config: dict
) -> pd.DataFrame:
    """Process raw motor data and calculate additional parameters.

    Takes raw data table, motor parameters, and data configuration,
    processes the data, and calculates additional electrical parameters.

    Args:
        raw_data: DataFrame containing raw measurement data.
        motor_params: Dictionary containing motor parameters (pole_pairs, rs_ohm).
        data_config: Dictionary containing column name configurations.

    Returns:
        Processed DataFrame with calculated columns.
    """
    processed_data = raw_data.copy()

    pole_pairs = motor_params["actual"]["pole_pairs"]
    stator_resistance = motor_params["actual"]["rs_ohm"]

    # Extract column names from config
    input_cols = data_config["data"]["standard_names"]["input"]
    comp_cols = data_config["data"]["standard_names"]["computed"]

    # Calculate electrical frequency
    processed_data[comp_cols["omega_e_rads"]] = processed_data[
        input_cols["speed_rpm"]
    ].apply(lambda speed: electrical_frequency(speed, pole_pairs))

    # Calculate flux linkages using voltage equation
    processed_data[comp_cols["psi_d_wb"]] = processed_data.apply(
        lambda row: flux_linkage_d_voltage(
            row[input_cols["uq_vpk"]],
            row[input_cols["iq_apk"]],
            row[comp_cols["omega_e_rads"]],
            stator_resistance,
        ),
        axis=1,
    )

    processed_data[comp_cols["psi_q_wb"]] = processed_data.apply(
        lambda row: flux_linkage_q_voltage(
            row[input_cols["ud_vpk"]],
            row[input_cols["id_apk"]],
            row[comp_cols["omega_e_rads"]],
            stator_resistance,
        ),
        axis=1,
    )

    # Calculate electromagnetic torque using flux linkage and current
    processed_data[comp_cols["torque_e_nm"]] = processed_data.apply(
        lambda row: torque_flux(
            row[comp_cols["psi_d_wb"]],
            row[comp_cols["psi_q_wb"]],
            row[input_cols["iq_apk"]],
            row[input_cols["id_apk"]],
            pole_pairs,
        ),
        axis=1,
    )

    # Calculate inductances
    # Note: We need psi_pm for Ld calculation. Assuming psi_wb from config/motor_params is the PM flux.
    psi_pm = motor_params["actual"]["psi_wb"]
    processed_data[comp_cols["ld_h"]] = processed_data.apply(
        lambda row: inductance_d(
            row[comp_cols["psi_d_wb"]],
            row[input_cols["id_apk"]],
            psi_pm,
        ),
        axis=1,
    )

    processed_data[comp_cols["lq_h"]] = processed_data.apply(
        lambda row: inductance_q(
            row[comp_cols["psi_q_wb"]],
            row[input_cols["iq_apk"]],
        ),
        axis=1,
    )

    # Calculate RMS values from peak values
    processed_data[comp_cols["id_arms"]] = processed_data[
        input_cols["id_apk"]
    ].apply(peak_to_rms)
    processed_data[comp_cols["iq_arms"]] = processed_data[
        input_cols["iq_apk"]
    ].apply(peak_to_rms)
    processed_data[comp_cols["ud_vrms"]] = processed_data[
        input_cols["ud_vpk"]
    ].apply(peak_to_rms)
    processed_data[comp_cols["uq_vrms"]] = processed_data[
        input_cols["uq_vpk"]
    ].apply(peak_to_rms)

    # Display first few rows of processed data
    print("Processed data head:")
    print(processed_data.head())

    return processed_data
