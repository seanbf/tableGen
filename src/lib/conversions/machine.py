"""Machine parameter conversion module.

This module provides functions for converting between different motor parameters,
such as Back EMF constant (Ke) and flux linkage (Psi).
"""

import math


def ke_to_psi(ke_v_krpm: float, pole_pairs: int) -> float:
    """Convert Back EMF constant to Permanent Magnet flux linkage.

    Args:
        ke_v_krpm: Back EMF constant in V_rms,LL / krpm.
        pole_pairs: Number of pole pairs.

    Returns:
        float: Permanent magnet flux linkage (psi_pm) in Weber-turns.

    Formula:
        V_peak,phase = psi_pm * omega_e
        omega_e = (RPM * pole_pairs * 2 * pi) / 60
        V_rms,LL = V_peak,phase * sqrt(3) / sqrt(2)
        Ke = V_rms,LL / (RPM / 1000)
        
        => psi_pm = (Ke * sqrt(2) * 60) / (sqrt(3) * 1000 * 2 * pi * pole_pairs)
        => psi_pm = (Ke * sqrt(6)) / (100 * pi * pole_pairs)
    """
    if pole_pairs <= 0:
        return 0.0
    
    return (ke_v_krpm * math.sqrt(6)) / (100 * math.pi * pole_pairs)


def psi_to_ke(psi_pm: float, pole_pairs: int) -> float:
    """Convert Permanent Magnet flux linkage to Back EMF constant.

    Args:
        psi_pm: Permanent magnet flux linkage (psi_pm) in Weber-turns.
        pole_pairs: Number of pole pairs.

    Returns:
        float: Back EMF constant in V_rms,LL / krpm.
    """
    if pole_pairs <= 0:
        return 0.0
        
    return (psi_pm * 100 * math.pi * pole_pairs) / math.sqrt(6)
