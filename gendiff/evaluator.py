# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""
from gendiff.loader import collect_data


def generate_diff(first_file_path, second_file_path, output_format='str'):
    """Generate diff function.

    Compares two files.

    Args:
        first_file_path (str): path to first file for comparison
        second_file_path (str): path to second file for comparison
        output_format (str, optional): output format. Defaults to 'str'.

    Returns:
        (str): output_format='str'
        (dic): {key:{status}}
    """
    first = collect_data(first_file_path)
    second = collect_data(second_file_path)
    compared = compare(first, second)
    if output_format == 'str':
        return str(compared)
    return compared


def compare(first, second):
    """[summary].

    [extended_summary]

    Args:
        first ([type]): [description]
        second ([type]): [description]

    Returns:
        [type]: [description]
    """
    compared = {}
    for key in sorted(first.keys() | second.keys()):
        first_value = first.get(key)
        second_value = second.get(key)
        removed(key, first, second, compared, first_value)
        added(key, second, first, compared, second_value)
        if key in first.keys() & second.keys():
            if isinstance(first_value, dict) and isinstance(second_value, dict):
                compared.update(
                    {key: compare(first_value, second_value)},
                )
                continue
            if first_value == second_value:
                compared.update(
                    {key: {'status': 'unchanged', 'value': first_value}},
                )
            else:
                compared.update(
                    {
                        key:
                        {
                            'status': 'updated',
                            'value': first_value,
                            'updated_value': second_value,
                        },
                    },
                )
    return compared


def removed(key, first, second, compared, first_value):
    """[summary].

    [extended_summary]

    Args:
        key ([type]): [description]
        first ([type]): [description]
        second ([type]): [description]
        compared ([type]): [description]
        first_value ([type]): [description]
    """
    if key in first.keys() - second.keys():
        compared.update(
            {key: {'status': 'removed', 'value': first_value}},
        )


def added(key, second, first, compared, second_value):
    """[summary].

    [extended_summary]

    Args:
        key ([type]): [description]
        second ([type]): [description]
        first ([type]): [description]
        compared ([type]): [description]
        second_value ([type]): [description]
    """
    if key in second.keys() - first.keys():
        compared.update(
            {key: {'status': 'added', 'value': second_value}},
        )
