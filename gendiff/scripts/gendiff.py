# -*- coding:utf-8 -*-
# TODO Docstrings
"""Difference Analyzer.

[extended_summary]

Returns:
    [type]: [description]

differences = { key: [old_value, new_value] }
    unchanged   -> old_value == new_value
    added       -> old_value == None
    removed     -> new_value == None
    updated     -> old_value != new_value
"""

import argparse
import json


def main():
    """[summary].

    [extended_summary]
    """
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    old_data = json.load(args.first_file)
    new_data = json.load(args.second_file)
    print_diff(compare_data(old_data, new_data))


def compare_data(old_data, new_data):
    """[summary].

    [extended_summary]

    Args:
        old_data ([type]): [description]
        new_data ([type]): [description]

    Returns:
        [type]: [description]
    """
    comparison = {}
    keys = sorted(old_data.keys() | new_data.keys())
    for key in keys:
        comparison[key] = [old_data.get(key), new_data.get(key)]
    return comparison


def generate_diff(file_path1, file_path2):
    """[summary].

    [extended_summary]

    Args:
        file_path1 ([type]): [description]
        file_path2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    diff = compare_data(
        collect_data_from_file(file_path1),
        collect_data_from_file(file_path2),
    )
    diff_str = ''
    for key in diff.keys():
        val1, val2 = diff[key]
        if val1 == val2:
            diff_str += '  {}: {};'.format(key, val1)
        elif not val2:
            diff_str += '- {}: {};'.format(key, val1)
        elif not val1:
            diff_str += '+ {}: {};'.format(key, val2)
        else:
            diff_str += '- {}: {};'.format(key, val1)
            diff_str += '+ {}: {};'.format(key, val2)
    return diff_str[:-1]


def collect_data_from_file(file_path):
    """[summary].

    [extended_summary]

    Args:
        file_path ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(file_path) as data_file:
        collected_data = json.load(data_file)
        data_file.close()
    return collected_data


def print_diff(diff):
    """[summary].

    [extended_summary]

    Args:
        diff ([type]): [description]
    """
    for key in diff.keys():
        val1, val2 = diff[key]
        if val1 == val2:
            print('  {}: {}'.format(key, val1))
        elif not val2:
            print('- {}: {}'.format(key, val1))
        elif not val1:
            print('+ {}: {}'.format(key, val2))
        else:
            print('- {}: {}'.format(key, val1))
            print('+ {}: {}'.format(key, val2))


if __name__ == '__main__':
    main()
