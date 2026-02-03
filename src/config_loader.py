"""Configuration loading module.

This module provides utilities for loading YAML configuration files
for the tableGen application.
"""

from pathlib import Path

import yaml


def load_config(config_path: str | None = None) -> dict:
    """Load YAML configuration file.

    Loads the tableGen configuration from a YAML file located in the
    config directory.

    Args:
        config_path: Optional path to config file. If None, uses default
                    config/config.yaml relative to project root.

    Returns:
        Dictionary containing the loaded configuration.

    Raises:
        FileNotFoundError: If configuration file is not found.
        yaml.YAMLError: If configuration file is malformed.

    Example:
        config = load_config()
        data_config = config['data']
    """
    if config_path is None:
        project_root = Path(__file__).parent.parent
        config_path = project_root / "config" / "config.yaml"
    else:
        config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    return config
