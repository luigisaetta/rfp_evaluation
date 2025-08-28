"""
utils
"""

import logging
import json


def get_console_logger(
    name: str = "console_logger", level=logging.INFO
) -> logging.Logger:
    """
    Create a console logger for debugging purposes.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def load_criteria_from_json(file_path: str) -> list[str]:
    """
    Load evaluation criteria from a JSON file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("criteria_list", [])
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
