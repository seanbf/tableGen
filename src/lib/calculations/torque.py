"""Electromagnetic torque calculations for synchronous machines.

This module provides functions for calculating electromagnetic torque using
both flux linkage-based and expanded d-q parameter formulations.
"""


def torque_flux(
    psi_d: float, psi_q: float, i_q: float, i_d: float, pole_pairs: int
) -> float:
    """Calculate electromagnetic torque using flux linkage and current.

    Calculates the electromagnetic torque using the standard formula:
    T = (3/2) * P * (ψd * iq - ψq * id)

    Args:
        psi_d: D-axis flux linkage in Weber-turns.
        psi_q: Q-axis flux linkage in Weber-turns.
        i_q: Q-axis current in Amperes.
        i_d: D-axis current in Amperes.
        pole_pairs: Number of pole pairs.

    Returns:
        Electromagnetic torque in Newton-meters (Nm).

    Formula:
        T = (3/2) * P * (ψd * iq - ψq * id)
    """
    return (3/2) * pole_pairs * (psi_d * i_q - psi_q * i_d)


def torque_idq(
    pole_pairs: int, psi_pm: float, ld: float, lq: float, i_d: float, i_q: float
) -> float:
    """Calculate electromagnetic torque using expanded torque equation.

    Calculates the electromagnetic torque for PMAC motors using the
    expanded torque equation:
    Te = (3/2) * p * (ψ * iq + (Ld - Lq) * id * iq)

    Args:
        pole_pairs: Number of pole pairs.
        psi_pm: Permanent magnet flux linkage in Weber-turns.
        ld: D-axis inductance in Henries.
        lq: Q-axis inductance in Henries.
        i_d: D-axis current in Amperes.
        i_q: Q-axis current in Amperes.

    Returns:
        Electromagnetic torque in Newton-meters (Nm).

    Formula:
        Te = (3/2) * p * (ψ * iq + (Ld - Lq) * id * iq)
    """
    return (3/2) * pole_pairs * (psi_pm * i_q + (ld - lq) * i_d * i_q)
