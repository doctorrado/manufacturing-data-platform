from pathlib import Path

import yaml


def load_config():
    project_root = Path(__file__).resolve().parent.parent.parent
    config_path = project_root / "config" / "config.yaml"

    try:
        with open(config_path, "r", encoding="utf-8") as stream:
            return yaml.safe_load(stream)

    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        ) from exc

    except yaml.YAMLError as exc:
        raise yaml.YAMLError(
            f"Failed to parse configuration file: {config_path}"
        ) from exc