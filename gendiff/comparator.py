# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""
from gendiff.loader import collect_data


def generate_diff(old_file_path, new_file_path, output_format='str'):
    """[summary].

    [extended_summary]

    Args:
        old_file_path ([type]): [description]
        new_file_path ([type]): [description]
        output_format (str, optional): [description]. Defaults to 'str'.

    Returns:
        [type]: [description]
    """
    old = collect_data(old_file_path)
    new = collect_data(new_file_path)
    compared = compare(old, new)
    if output_format == 'str':
        return str(compared)
    return compared


def compare(old, new):
    """[summary].

    [extended_summary]

    Args:
        old ([type]): [description]
        new ([type]): [description]

    Returns:
        [type]: [description]
    """
    compared = {}
    compared_value = {}
    for key in sorted(old.keys() | new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        if key in old.keys() - new.keys():
            compared_value = {
                'status': 'removed',
                'value': old_value,
            }
        if key in new.keys() - old.keys():
            compared_value = {
                'status': 'added',
                'value': new_value,
            }
        if key in old.keys() & new.keys():
            compared_value = compare_same_keys(old_value, new_value)
        compared[key] = compared_value
    return compared


def compare_same_keys(old_value, new_value):
    """[summary].

    [extended_summary]

    Args:
        old_value ([type]): [description]
        new_value ([type]): [description]

    Returns:
        [type]: [description]
    """
    if old_value == new_value:
        return {
            'status': 'unchanged',
            'value': old_value,
        }
    elif isinstance(old_value, dict) and isinstance(new_value, dict):
        return compare(old_value, new_value)
    return {
        'status': 'updated',
        'value': old_value,
        'updated_value': new_value,
    }
