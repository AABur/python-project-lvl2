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
    print(render(diff))


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


def compare(first, second):  # noqa:C901
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
        if key in first.keys() - second.keys():
            compared.update(
                {key: {'status': 'removed', 'value': first_value}},
            )
        if key in second.keys() - first.keys():
            compared.update(
                {key: {'status': 'added', 'value': second_value}},
            )
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
                            'old_value': first_value,
                            'new_value': second_value,
                        },
                    },
                )
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
        collected = get_loader(ext)(data_file)
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


def render(source, indent=0):  # noqa:WPS210
    """[summary].

    [extended_summary]

    Args:
        source ([type]): [description]
        indent (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """
    lf_char = '\n'
    ht_char = ' '
    nlch = lf_char + ht_char * (indent + 4)
    if isinstance(source, dict):
        output_items = []
        for key in source:
            output_value = source.get(key)
            status = output_value.get('status', '') if isinstance(
                output_value, dict,
            ) else ''
            if status:
                output_value = output_value.get('value')
            output_items.append(
                '{}{}{}: {}'.format(
                    nlch,
                    STATUSES.get(status, ''),
                    key,
                    render(output_value, indent + 4),
                ),
            )
        return '{{{}}}'.format(
            ''.join(output_items) + lf_char + ht_char * indent,
        )
    return source


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


STATUSES = {  # noqa:WPS407
    'added': '+ ',
    'removed': '- ',
    'unchanged': '  ',
    'updated': '+-',
}


if __name__ == '__main__':
    main()
