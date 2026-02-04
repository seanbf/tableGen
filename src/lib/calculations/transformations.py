"""Coordinate transformation utilities for vector control.

This module provides Clarke and Park transformations (and their inverses)
used to convert between stationary three-phase, stationary two-phase,
and rotating two-phase reference frames.
"""

import math
from typing import Tuple, Union


def clarke_transform(
    current_a: Union[float, list],
    current_b: Union[float, list],
    current_c: Union[float, list],
) -> Tuple[Union[float, list], Union[float, list]]:
    """Perform Clarke transformation on three-phase currents.

    Converts three-phase currents to alpha-beta components using the Clarke
    transformation. This transformation converts three-phase quantities to a
    stationary reference frame.

    Args:
        current_a: Phase A current in Amperes.
        current_b: Phase B current in Amperes.
        current_c: Phase C current in Amperes.

    Returns:
        Tuple of (alpha, beta) components in Amperes.

    Formula:
        alpha = Ia
        beta = (Ib - Ic) / √3
    """
    alpha = current_a
    beta = (current_b - current_c) / math.sqrt(3)
    return alpha, beta


def inverse_clarke_transform(
    alpha: Union[float, list], beta: Union[float, list]
) -> Tuple[Union[float, list], Union[float, list], Union[float, list]]:
    """Perform inverse Clarke transformation.

    Converts alpha-beta components back to three-phase quantities.

    Args:
        alpha: Alpha component (direct component) in Amperes.
        beta: Beta component (quadrature component) in Amperes.

    Returns:
        Tuple of (phase_a, phase_b, phase_c) currents in Amperes.

    Formula:
        Ia = alpha
        Ib = -0.5 * alpha + (√3/2) * beta
        Ic = -0.5 * alpha - (√3/2) * beta
    """
    phase_a = alpha
    phase_b = (-0.5 * alpha) + (math.sqrt(3) / 2) * beta
    phase_c = (-0.5 * alpha) - (math.sqrt(3) / 2) * beta
    return phase_a, phase_b, phase_c


def park_transform(
    alpha: Union[float, list],
    beta: Union[float, list],
    theta: Union[float, list],
) -> Tuple[Union[float, list], Union[float, list]]:
    """Perform Park transformation on alpha-beta components.

    Converts alpha-beta components to d-q components using Park
    transformation. This transformation converts stationary reference frame
    quantities to rotating reference frame quantities.

    Args:
        alpha: Alpha component (direct component) in Amperes.
        beta: Beta component (quadrature component) in Amperes.
        theta: Electrical angle in radians.

    Returns:
        Tuple of (d_component, q_component) in Amperes.

    Formula:
        d = alpha * cos(θ) + beta * sin(θ)
        q = -alpha * sin(θ) + beta * cos(θ)
    """
    d_component = alpha * math.cos(theta) + beta * math.sin(theta)
    q_component = -alpha * math.sin(theta) + beta * math.cos(theta)
    return d_component, q_component


def inverse_park_transform(
    d_component: Union[float, list],
    q_component: Union[float, list],
    theta: Union[float, list],
) -> Tuple[Union[float, list], Union[float, list]]:
    """Perform inverse Park transformation.

    Converts d-q components back to alpha-beta components.

    Args:
        d_component: D-axis component (direct axis) in Amperes.
        q_component: Q-axis component (quadrature axis) in Amperes.
        theta: Electrical angle in radians.

    Returns:
        Tuple of (alpha, beta) components in Amperes.

    Formula:
        alpha = d * cos(θ) - q * sin(θ)
        beta = d * sin(θ) + q * cos(θ)
    """
    alpha = d_component * math.cos(theta) - q_component * math.sin(theta)
    beta = d_component * math.sin(theta) + q_component * math.cos(theta)
    return alpha, beta
