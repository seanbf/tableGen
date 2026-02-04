"""Voltage and current conversions.

This module provides functions for converting between different voltage and
current representations, such as peak to RMS conversions.
"""

import math


def peak_to_rms(peak_value: float) -> float:
    """Convert peak value to RMS value.

    Converts a peak value to its RMS (Root Mean Square) equivalent
    for sinusoidal waveforms.

    Args:
        peak_value: Peak value of the waveform.

    Returns:
        RMS value of the waveform.

    Formula:
        rms_value = peak_value / √2

    Examples:
        >>> peak_to_rms(331.3)  # 331.3 V peak = 234 V RMS
        234.0
        >>> peak_to_rms(14.14)  # 14.14 A peak = 10 A RMS
        10.0
    """
    # For sinusoidal waveforms: RMS = Peak / √2
    return peak_value / math.sqrt(2)


def rms_to_peak(rms_value: float) -> float:
    """Convert RMS value to peak value.

    Converts an RMS (Root Mean Square) value to its peak equivalent
    for sinusoidal waveforms.

    Args:
        rms_value: RMS value of the waveform.

    Returns:
        Peak value of the waveform.

    Formula:
        peak_value = rms_value * √2

    Examples:
        >>> rms_to_peak(234)    # 234 V RMS = 331.3 V peak
        331.3
        >>> rms_to_peak(10)     # 10 A RMS = 14.14 A peak
        14.14
    """
    # For sinusoidal waveforms: Peak = RMS * √2
    return rms_value * math.sqrt(2)
