import os
import yaml
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads a yaml file and returns
    Args: path_to_yaml (Path): path like input
    Raise: ValueError: if yaml file is empty, e: empty file
    Returns: ConfigBox: ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Reading yaml file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Empty yaml file: {path_to_yaml}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates directories if they don't exist
    Args: path_to_directories (list): list of paths to directories
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")