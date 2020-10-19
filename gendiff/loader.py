# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os

import yaml


def get_loader(loader):
    """Call data loader.

    Call the loader according to the file extension

    Args:
        loader (str): file extention

    Returns:
        fucnction: file loader
    """
    return {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(loader)


def collect_data(file_path):
    """Collect data from file.

    Args:
        file_path (str): path to JSON or YAML file

    Returns:
        (dict): decoded data
    """
    with open(file_path) as data_file:
        _, ext = os.path.splitext(file_path)
        collected = get_loader(ext)(data_file)
    return collected
