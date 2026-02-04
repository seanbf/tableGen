"""Motor parameter acquisition and validation module.

This module provides functions for obtaining motor parameters from user input,
including converting Back EMF constant (Ke) to flux linkage.
"""
from src.lib.conversions.machine import ke_to_psi


def get_motor_parameters(motor_config: dict) -> dict:
    """Get motor parameters from user input with defaults.

    Prompts the user to enter motor parameters including pole pairs,
    stator resistance, and Back EMF constant (Ke). Calculates
    permanent magnet flux linkage from the provided Ke.

    Args:
        motor_config: Dictionary containing default motor parameters and
                     validation rules.

    Returns:
        Dictionary containing motor parameters with:
            - pole_pairs: Number of pole pairs in the motor
            - rs_ohm: Stator resistance in Ohms
            - ke_v_krpm: Back EMF constant in V_rms,LL / krpm
            - psi_wb: Calculated flux linkage in Weber-turns

    Example:
        motor_params = get_motor_parameters(motor_config)
    """
    motor_params = motor_config["motor"]

    # Prompt user for pole pairs
    default_pole_pairs = motor_params["pole_pairs"]
    user_input = input(
        f"Enter number of pole pairs [{default_pole_pairs} Pole Pairs]: "
    )
    pole_pairs = int(user_input) if user_input.strip() else default_pole_pairs

    # Prompt user for stator resistance
    default_stator_resistance = motor_params["rs_ohm"]
    user_input = input(
        f"Enter stator resistance in Ohms [{default_stator_resistance} Ohms]: "
    )
    stator_resistance = (
        float(user_input) if user_input.strip() else default_stator_resistance
    )

    # Prompt user for Ke
    default_ke = motor_params["ke_v_krpm"]
    user_input = input(
        f"Enter Back EMF constant in V_rms,LL / krpm [{default_ke} Ke]: "
    )
    ke_v_krpm = float(user_input) if user_input.strip() else default_ke

    # Calculate Psi from Ke
    psi_wb = ke_to_psi(ke_v_krpm, pole_pairs)

    # Display selected parameters
    print(f"Using pole pairs: {pole_pairs} Pole Pairs")
    print(f"Using stator resistance: {stator_resistance} Ohms")
    print(f"Using Back EMF constant: {ke_v_krpm} V_rms/krpm")
    print(f"Calculated PM flux linkage: {psi_wb:.6f} Wb")

    return {
        "actual": {
            "pole_pairs": pole_pairs,
            "rs_ohm": stator_resistance,
            "ke_v_krpm": ke_v_krpm,
            "psi_wb": psi_wb,
        }
    }
