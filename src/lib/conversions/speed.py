"""Rotational speed conversions.

This module provides functions for converting between different rotational
speed units, such as RPM to rad/s conversions.
"""

import math


def rpm2rads(rpm: float) -> float:
    """Convert RPM to radians per second.

    Converts rotational speed from revolutions per minute (RPM)
    to radians per second (rad/s).

    Args:
        rpm: Rotational speed in revolutions per minute.

    Returns:
        Rotational speed in radians per second.

    Formula:
        rads = rpm * (2π / 60)

    Examples:
        >>> rpm2rads(1800)  # 1800 RPM = 188.5 rad/s
        188.5
    """
    # Convert RPM to rad/s: 1 revolution = 2π radians, 1 minute = 60 seconds
    return rpm * (2 * math.pi / 60)


def rads2rpm(rads: float) -> float:
    """Convert radians per second to RPM.

    Converts rotational speed from radians per second (rad/s)
    to revolutions per minute (RPM).

    Args:
        rads: Rotational speed in radians per second.

    Returns:
        Rotational speed in revolutions per minute.

    Formula:
        rpm = rads * (60 / 2π)

    Examples:
        >>> rads2rpm(188.5)  # 188.5 rad/s = 1800 RPM
        1800.0
    """
    # Convert rad/s to RPM: 1 revolution = 2π radians, 1 minute = 60 seconds
    return rads * (60 / (2 * math.pi))
