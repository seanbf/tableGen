"""Electrical power calculations.

This module provides functions for calculating various electrical power metrics
including apparent power, real power, reactive power, and power factor.
"""


def apparent_power(voltage_rms: float, current_rms: float) -> float:
    """Calculate apparent power using RMS voltage and current.

    Calculates the apparent power in Volt-Amperes (VA) using the standard
    electrical engineering formula.

    Args:
        voltage_rms: RMS voltage in Volts.
        current_rms: RMS current in Amperes.

    Returns:
        Apparent power in Volt-Amperes (VA).

    Formula:
        S = Urms * Irms
    """
    return voltage_rms * current_rms


def electrical_power(
    voltage_rms: float, current_rms: float, power_factor: float
) -> float:
    """Calculate real electrical power.

    Calculates the real electrical power in Watts using RMS voltage, RMS
    current, and power factor.

    Args:
        voltage_rms: RMS voltage in Volts.
        current_rms: RMS current in Amperes.
        power_factor: Power factor (dimensionless, 0-1).

    Returns:
        Real electrical power in Watts.

    Formula:
        P = Urms * Irms * cos(φ)
    """
    return voltage_rms * current_rms * power_factor


def reactive_power(apparent_power: float, real_power: float) -> float:
    """Calculate reactive power.

    Calculates the reactive power in Volt-Amperes Reactive (VAR) using
    apparent and real power.

    Args:
        apparent_power: Apparent power in Volt-Amperes (VA).
        real_power: Real power in Watts.

    Returns:
        Reactive power in Volt-Amperes Reactive (VAR).

    Formula:
        Q = √(S² - P²)
    """
    import math

    return math.sqrt(apparent_power**2 - real_power**2)


def power_factor(real_power: float, apparent_power: float) -> float:
    """Calculate power factor.

    Calculates the power factor from real and apparent power, constrained
    to the range [0, 1].

    Args:
        real_power: Real power in Watts.
        apparent_power: Apparent power in Volt-Amperes (VA).

    Returns:
        Power factor (dimensionless, range 0-1).

    Formula:
        PF = P / S
    """
    if apparent_power == 0:
        return 0.0
    return max(0.0, min(1.0, real_power / apparent_power))
