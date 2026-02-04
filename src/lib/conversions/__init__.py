"""Conversions package for electrical and mechanical units.

This package provides utility functions for converting between different
units commonly used in electrical engineering and motor control.

Submodules:
    - waveform: Voltage and current conversions (peak, RMS)
    - speed: Rotational speed conversions (RPM, rad/s)
"""

from src.lib.conversions.speed import rads_to_rpm, rpm_to_rads
from src.lib.conversions.waveform import peak_to_rms, rms_to_peak

__all__ = [
    "peak_to_rms",
    "rms_to_peak",
    "rpm_to_rads",
    "rads_to_rpm",
]
