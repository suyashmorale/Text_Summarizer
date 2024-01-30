import os
import logging
import yaml
from textsummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read yaml file and returns
    
    Args:
        path_to_yaml (Path): path like input
    
    Raises:
        ValueError: if yaml file is empty

    Returns:
        ConfigBox: returns ConfigBox object
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"Yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for dir_path in path_to_directories:
        os.makedirs(dir_path, exist_ok=True)
        logger.info(f"directory created at {dir_path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in kb

    Args:
        path (Path): path of file
    
    Returns:
        str: size in kb
    """
    
    size_in_kb = round(os.path.getsize(path) / (1024))
    return f"~{size_in_kb} KB"