"""Flux linkage calculations for electrical machines.

This module provides functions for calculating flux linkage in d-axis and q-axis
reference frames, both from inductance and current, and from voltage equations.
"""


def flux_linkage_d(i_d: float, ld: float) -> float:
    """Calculate d-axis flux linkage.

    Calculates the d-axis flux linkage from d-axis current and inductance.

    Args:
        i_d: D-axis current in Amperes.
        ld: D-axis inductance in Henries.

    Returns:
        D-axis flux linkage in Weber-turns.

    Formula:
        ψd = Ld * id
    """
    return ld * i_d


def flux_linkage_q(i_q: float, lq: float) -> float:
    """Calculate q-axis flux linkage.

    Calculates the q-axis flux linkage from q-axis current and inductance.

    Args:
        i_q: Q-axis current in Amperes.
        lq: Q-axis inductance in Henries.

    Returns:
        Q-axis flux linkage in Weber-turns.

    Formula:
        ψq = Lq * iq
    """
    return lq * i_q


def flux_linkage_d_voltage(
    u_q: float, i_q: float, omega_e: float, rs: float
) -> float:
    """Calculate d-axis flux linkage using voltage equation.

    Calculates the d-axis flux linkage from q-axis voltage and current
    using the dq-reference frame voltage equation: v = R*i + dλ/dt.
    This represents the coupling between d and q axes.

    Args:
        u_q: Q-axis voltage in Volts.
        i_q: Q-axis current in Amperes.
        omega_e: Electrical frequency in rad/s.
        rs: Stator resistance in Ohms.

    Returns:
        D-axis flux linkage in Weber-turns.

    Formula:
        ψd = -((Rs * iq) - uq) / ωe
    """
    return -1 * ((rs * i_q) - u_q) / omega_e


def flux_linkage_q_voltage(
    u_d: float, i_d: float, omega_e: float, rs: float
) -> float:
    """Calculate q-axis flux linkage using voltage equation.

    Calculates the q-axis flux linkage from d-axis voltage and current
    using the dq-reference frame voltage equation: v = R*i + dλ/dt.
    This represents the coupling between q and d axes.

    Args:
        u_d: D-axis voltage in Volts.
        i_d: D-axis current in Amperes.
        omega_e: Electrical frequency in rad/s.
        rs: Stator resistance in Ohms.

    Returns:
        Q-axis flux linkage in Weber-turns.

    Formula:
        ψq = ((Rs * id) - ud) / ωe
    """
    return ((rs * i_d) - u_d) / omega_e
