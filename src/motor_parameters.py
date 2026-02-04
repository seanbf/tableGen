"""Motor parameter acquisition and validation module.

This module provides functions for obtaining motor parameters from user input
with configurable defaults and validation rules.
"""


def get_motor_parameters(motor_config: dict) -> dict:
    """Get motor parameters from user input with defaults.

    Prompts the user to enter motor parameters with sensible defaults
    and returns them in a structure.

    Args:
        motor_config: Dictionary containing default motor parameters and
                     validation rules.

    Returns:
        Dictionary containing motor parameters with:
            - pole_pairs: Number of pole pairs in the motor
            - rs_ohm: Stator resistance in Ohms

    Example:
        motor_params = get_motor_parameters(motor_config)
        print(f"Pole pairs: {motor_params['pole_pairs']}")
    """
    defaults = motor_config["motor"]["defaults"]

    # Prompt user for pole pairs
    default_pole_pairs = defaults["pole_pairs"]
    user_input = input(
        f"Enter number of pole pairs [{default_pole_pairs} Pole Pairs]: "
    )
    pole_pairs = int(user_input) if user_input.strip() else default_pole_pairs

    # Prompt user for stator resistance
    default_stator_resistance = defaults["rs_ohm"]
    user_input = input(
        f"Enter stator resistance in Ohms [{default_stator_resistance} Ohms]: "
    )
    stator_resistance = (
        float(user_input) if user_input.strip() else default_stator_resistance
    )

    # Display selected parameters
    print(f"Using pole pairs: {pole_pairs} Pole Pairs")
    print(f"Using stator resistance: {stator_resistance} Ohms")

    return {
        "actual": {
            "pole_pairs": pole_pairs,
            "rs_ohm": stator_resistance,
        }
    }
