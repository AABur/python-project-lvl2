# -*- coding:utf-8 -*-
"""Generate diff.

Compares two configuration files.

CLI usage:
gendiff [-h] [-f FORMAT] first_file second_file

function usage:
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2)
"""
import argparse
import json
import os

import yaml

LOADER = {  # noqa:WPS407
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}


def main():
    """Generate diff CLI.

    CLI usage: gendiff [-h] [-f FORMAT] first_file second_file
    """
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = (generate_diff(args.first_file.name, args.second_file.name, 'dict'))
    print(json.dumps(diff, indent=4))


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
    first = collect_from_file(first_file_path)
    second = collect_from_file(second_file_path)
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
        if key in first.keys() - second.keys():
            compared[key] = {
                'status': 'removed',
                'value': first.get(key),
            }
        if key in second.keys() - first.keys():
            compared[key] = {
                'status': 'added',
                'value': second.get(key),
            }
        if key in first.keys() & second.keys():
            if first.get(key) == second.get(key):
                compared[key] = {
                    'status': 'unchanged',
                    'value': first.get(key),
                }
            else:
                compared[key] = {
                    'status': 'updated',
                    'old_value': first.get(key),
                    'new_value': second.get(key),
                }
    return compared


def collect_from_file(file_path):
    """Collect data from json file.

    Args:
        file_path (syr): path to file

    Returns:
        dict: collected data
    """
    with open(file_path) as data_file:
        _, ext = os.path.splitext(file_path)
        collected = LOADER.get(ext)(data_file)
        data_file.close()
    return collected


def flatten(nested):
    """[summary].

    [extended_summary]

    Args:
        nested (dict): [description]

    Returns:
        (dict): [description]
    """
    flatted = {}
    for k1, v1 in nested.items():
        if isinstance(v1, dict):
            if not v1:
                flatted[k1] = ''
            for k2, v2 in flatten(v1).items():
                flatted['{0}/{1}'.format(k1, k2)] = v2
        else:
            flatted[k1] = v1
    return flatted


if __name__ == '__main__':
    main()
