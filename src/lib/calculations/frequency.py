"""Frequency and speed conversion calculations.

This module provides functions for converting between mechanical speed (RPM)
and electrical frequency (Hz, rad/s), accounting for motor pole pairs.
"""

import math


def electrical_frequency(
    mechanical_speed_rpm: float, pole_pairs: int
) -> float:
    """Calculate electrical frequency from mechanical speed.

    Converts mechanical speed in RPM to electrical frequency in radians
    per second based on the number of pole pairs.

    Args:
        mechanical_speed_rpm: Mechanical speed in revolutions per minute.
        pole_pairs: Number of pole pairs in the motor.

    Returns:
        Electrical frequency in radians per second (rad/s).

    Formula:
        f_elec = (mechanical_speed * pole_pairs) * (2π/60)
    """
    return abs(mechanical_speed_rpm) * pole_pairs * (2 * math.pi / 60)


def synchronous_speed(
    frequency_hz: float, pole_pairs: int
) -> float:
    """Calculate synchronous speed from frequency and pole pairs.

    Converts electrical frequency in Hertz to synchronous speed in RPM
    based on the number of pole pairs.

    Args:
        frequency_hz: Electrical frequency in Hertz (Hz).
        pole_pairs: Number of pole pairs in the motor.

    Returns:
        Synchronous speed in revolutions per minute (RPM).

    Formula:
        sync_speed = (120 * frequency) / (2 * pole_pairs)
    """
    return (120 * frequency_hz) / (2 * pole_pairs)
