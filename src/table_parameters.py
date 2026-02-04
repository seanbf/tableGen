"""Table generation parameter acquisition and validation module.

This module provides functions for obtaining table generation parameters
from user input with configurable defaults and validation rules.
"""


def get_table_parameters(table_config: dict) -> dict:
    """Get table parameters from user input with defaults.

    Prompts the user to enter table generation parameters with sensible
    defaults and returns them in a structure.

    Args:
        table_config: Dictionary containing default table parameters and
                     validation rules.

    Returns:
        Dictionary containing table generation parameters with:
            - size: Grid resolution (rows/columns)
            - max_current_a: Maximum current for table generation (Amps)

    Example:
        table_params = get_table_parameters(table_config)
        print(f"Table size: {table_params['size']}")
    """
    table_params = table_config["table"]

    # Prompt user for table size
    default_size = table_params["size"]
    user_input = input(f"Enter Table Size [{default_size}]: ")

    if user_input.strip():
        try:
            size = int(user_input)
        except ValueError:
            size = default_size
            print(f"Invalid input. Using default table size: {default_size}")
    else:
        size = default_size

    # Prompt user for maximum current
    default_max_current = table_params["max_current_a"]
    user_input = input(
        f"Enter Maximum Current for Table Generation (A) [{default_max_current}]: "
    )

    if user_input.strip():
        try:
            max_current = float(user_input)
        except ValueError:
            max_current = default_max_current
            print(
                f"Invalid input. Using default maximum current: {default_max_current} A"
            )
    else:
        max_current = default_max_current

    return {
        "size": size,
        "max_current_a": max_current,
    }
