"""Conversions package for electrical and mechanical units.

This package provides utility functions for converting between different
units commonly used in electrical engineering and motor control.

Submodules:
    - waveform: Voltage and current conversions (peak, RMS)
    - speed: Rotational speed conversions (RPM, rad/s)
"""

from src.lib.conversions.speed import rads2rpm, rpm2rads
from src.lib.conversions.waveform import peak2rms, rms2peak

__all__ = [
    "peak2rms",
    "rms2peak",
    "rpm2rads",
    "rads2rpm",
]
