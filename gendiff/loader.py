# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
from os import error

import yaml


def collect_data(file_path):
    """Collect data from file.

    Args:
        file_path(str): path to JSON or YAML file

    Raises:
        error: [description]

    Returns:
        (dict): decoded data
    """
    loaders = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    call_loader = loaders.get
    correct_exts = loaders.keys()
    _, ext = os.path.splitext(file_path)
    if ext not in correct_exts:
        raise error('Wrong file')
    with open(file_path) as data_file:
        return call_loader(ext)(data_file)
