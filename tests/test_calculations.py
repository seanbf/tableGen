"""Unit tests for motor calculations."""

import pytest

from src.lib.calculations.inductance import (
    inductance_d,
    inductance_d_voltage,
    inductance_q,
    inductance_q_voltage,
)


def test_inductance_d():
    """Test d-axis inductance calculation from flux."""
    # Ld = (psi_d - psi_pm) / i_d
    # (0.1 - 0.05) / 10 = 0.005
    assert inductance_d(0.1, 10.0, 0.05) == pytest.approx(0.005)
    # Negative i_d (weakening)
    # (0.04 - 0.05) / -2 = -0.01 / -2 = 0.005
    assert inductance_d(0.04, -2.0, 0.05) == pytest.approx(0.005)
    # Zero current
    assert inductance_d(0.05, 0.0, 0.05) == 0.0


def test_inductance_q():
    """Test q-axis inductance calculation from flux."""
    # Lq = psi_q / i_q
    # 0.2 / 10 = 0.02
    assert inductance_q(0.2, 10.0) == pytest.approx(0.02)
    # Zero current
    assert inductance_q(0.2, 0.0) == 0.0


def test_inductance_d_voltage():
    """Test d-axis inductance calculation from voltage equations."""
    # Ld = (u_q - rs*i_q - omega_e*psi_pm) / (omega_e*i_d)
    # u_q=100, rs=0.1, i_q=10, omega_e=100, psi_pm=0.05, i_d=20
    # numerator = 100 - (0.1*10) - (100*0.05) = 100 - 1 - 5 = 94
    # denominator = 100 * 20 = 2000
    # Ld = 94 / 2000 = 0.047
    result = inductance_d_voltage(100.0, 10.0, 100.0, 0.1, 0.05, 20.0)
    assert result == pytest.approx(0.047)
    # Zero frequency/current denominator
    assert inductance_d_voltage(100.0, 10.0, 0.0, 0.1, 0.05, 20.0) == 0.0


def test_inductance_q_voltage():
    """Test q-axis inductance calculation from voltage equations."""
    # Lq = (rs*i_d - u_d) / (omega_e*i_q)
    # rs=0.1, i_d=10, u_d=-50, omega_e=100, i_q=20
    # numerator = (0.1*10) - (-50) = 1 + 50 = 51
    # denominator = 100 * 20 = 2000
    # Lq = 51 / 2000 = 0.0255
    assert inductance_q_voltage(-50.0, 10.0, 100.0, 0.1, 20.0) == pytest.approx(0.0255)
    # Zero frequency/current denominator
    assert inductance_q_voltage(-50.0, 10.0, 100.0, 0.1, 0.0) == 0.0
