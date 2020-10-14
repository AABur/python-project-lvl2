# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]

Returns:
    [type]: [description]
"""

import json
import os

import yaml


def get_loader(loader):
    """[summary].

    [extended_summary]

    Args:
        loader ([type]): [description]

    Returns:
        [type]: [description]
    """
    return {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(loader)


def collect_data(file_path):
    """Collect data from json file.

    Args:
        file_path (syr): path to file

    Returns:
        dict: collected data
    """
    with open(file_path) as data_file:
        _, ext = os.path.splitext(file_path)
        collected = get_loader(ext)(data_file)
        data_file.close()
    return collected
