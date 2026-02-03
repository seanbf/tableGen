"""Flux linkage calculations for electrical machines.

This module provides functions for calculating flux linkage in d-axis and q-axis
reference frames, both from inductance and current, and from voltage equations.
"""


def flux_linkage_d_axis(d_axis_current: float, inductance_d: float) -> float:
    """Calculate d-axis flux linkage.

    Calculates the d-axis flux linkage from d-axis current and inductance.

    Args:
        d_axis_current: D-axis current in Amperes.
        inductance_d: D-axis inductance in Henries.

    Returns:
        D-axis flux linkage in Weber-turns.

    Formula:
        λd = Ld * Id
    """
    return inductance_d * d_axis_current


def flux_linkage_q_axis(q_axis_current: float, inductance_q: float) -> float:
    """Calculate q-axis flux linkage.

    Calculates the q-axis flux linkage from q-axis current and inductance.

    Args:
        q_axis_current: Q-axis current in Amperes.
        inductance_q: Q-axis inductance in Henries.

    Returns:
        Q-axis flux linkage in Weber-turns.

    Formula:
        λq = Lq * Iq
    """
    return inductance_q * q_axis_current


def calculate_flux_linkage_d_axis(
    voltage_q_axis: float, current_q_axis: float,
    electrical_frequency_rads: float, stator_resistance: float
) -> float:
    """Calculate d-axis flux linkage using voltage equation.

    Calculates the d-axis flux linkage from q-axis voltage and current
    using the dq-reference frame voltage equation: v = R*i + dλ/dt.
    This represents the coupling between d and q axes.

    Args:
        voltage_q_axis: Q-axis voltage in Volts.
        current_q_axis: Q-axis current in Amperes.
        electrical_frequency_rads: Electrical frequency in rad/s.
        stator_resistance: Stator resistance in Ohms.

    Returns:
        D-axis flux linkage in Weber-turns.

    Formula:
        λd = -((Rs * Iq) - Vq) / ωe
    """
    return -1 * ((stator_resistance * current_q_axis) - voltage_q_axis) / \
           electrical_frequency_rads


def calculate_flux_linkage_q_axis(
    voltage_d_axis: float, current_d_axis: float,
    electrical_frequency_rads: float, stator_resistance: float
) -> float:
    """Calculate q-axis flux linkage using voltage equation.

    Calculates the q-axis flux linkage from d-axis voltage and current
    using the dq-reference frame voltage equation: v = R*i + dλ/dt.
    This represents the coupling between q and d axes.

    Args:
        voltage_d_axis: D-axis voltage in Volts.
        current_d_axis: D-axis current in Amperes.
        electrical_frequency_rads: Electrical frequency in rad/s.
        stator_resistance: Stator resistance in Ohms.

    Returns:
        Q-axis flux linkage in Weber-turns.

    Formula:
        λq = ((Rs * Id) - Vd) / ωe
    """
    return ((stator_resistance * current_d_axis) - voltage_d_axis) / \
           electrical_frequency_rads
