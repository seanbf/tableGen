"""Electromagnetic torque calculations.

This module provides functions for calculating electromagnetic torque using
various formulations including flux linkage-based and expanded d-q methods.
"""


def calculate_torque_flux_nm(
    flux_linkage_d_axis_wb: float, flux_linkage_q_axis_wb: float,
    current_q_axis_a: float, current_d_axis_a: float, pole_pairs: int
) -> float:
    """Calculate electromagnetic torque using flux linkage and current.

    Calculates the electromagnetic torque using the standard formula:
    T = (3/2) * P * (λd * iq - λq * id)

    Args:
        flux_linkage_d_axis_wb: D-axis flux linkage in Weber-turns.
        flux_linkage_q_axis_wb: Q-axis flux linkage in Weber-turns.
        current_q_axis_a: Q-axis current in Amperes.
        current_d_axis_a: D-axis current in Amperes.
        pole_pairs: Number of pole pairs.

    Returns:
        Electromagnetic torque in Newton-meters (Nm).

    Formula:
        T = (3/2) * P * (λd * Iq - λq * Id)
    """
    return (3/2) * pole_pairs * (
        flux_linkage_d_axis_wb * current_q_axis_a -
        flux_linkage_q_axis_wb * current_d_axis_a
    )


def calculate_torque_torque_idq_nm(
    pole_pairs: int, flux_linkage_wb: float,
    d_axis_inductance_h: float, q_axis_inductance_h: float,
    current_d_axis_a: float, current_q_axis_a: float
) -> float:
    """Calculate electromagnetic torque using expanded torque equation.

    Calculates the electromagnetic torque for PMAC motors using the
    expanded torque equation:
    Te = (3/2) * p * (λ * Iq + (Ld - Lq) * Id * Iq)

    Args:
        pole_pairs: Number of pole pairs.
        flux_linkage_wb: Flux linkage in Weber-turns.
        d_axis_inductance_h: D-axis inductance in Henries.
        q_axis_inductance_h: Q-axis inductance in Henries.
        current_d_axis_a: D-axis current in Amperes.
        current_q_axis_a: Q-axis current in Amperes.

    Returns:
        Electromagnetic torque in Newton-meters (Nm).

    Formula:
        Te = (3/2) * p * (λ * Iq + (Ld - Lq) * Id * Iq)
    """
    return (3/2) * pole_pairs * (
        flux_linkage_wb * current_q_axis_a +
        (d_axis_inductance_h - q_axis_inductance_h) *
        current_d_axis_a * current_q_axis_a
    )
