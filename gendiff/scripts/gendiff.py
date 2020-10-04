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


def main():
    """Generate diff CLI.

    CLI usage: gendiff [-h] [-f FORMAT] first_file second_file
    """
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = (generate_diff(args.first_file.name, args.second_file.name))
    print(diff.replace(';', '\n'))


def generate_diff(first_file_path, second_file_path):
    """Generate diff function.

    Compares two files.

    Args:
        first_file_path (str): path to first file for comparison
        second_file_path (str): path to second file for comparison

    Returns:
        (str): string with differences
    """
    combined_data = combine_data(
        collect_data_from_file(first_file_path),
        collect_data_from_file(second_file_path),
    )
    difference = ''
    for key in combined_data.keys():
        val1, val2 = combined_data[key]
        if val1 == val2:
            difference += '  {}: {};'.format(key, val1)
        elif not val2:
            difference += '- {}: {};'.format(key, val1)
        elif not val1:
            difference += '+ {}: {};'.format(key, val2)
        else:
            difference += '- {}: {};'.format(key, val1)
            difference += '+ {}: {};'.format(key, val2)
    return difference[:-1]


def combine_data(first_data, second_data):
    """Combine two dictionaries.

    Args:
        first_data (dict): first dictionary {key1: value1}
        second_data (dict): second dictionary {key2: value2}

    Returns:
        dict: combined dictionary {key: [value1/None, value2/None]}
    """
    combined_data = {}
    keys = sorted(first_data.keys() | second_data.keys())
    for key in keys:
        combined_data[key] = [first_data.get(key), second_data.get(key)]
    return combined_data


def collect_data_from_file(file_path):
    """Collect data from json file.

    Args:
        file_path (syr): path to file

    Returns:
        dict: collected data
    """
    with open(file_path) as data_file:
        collected_data = json.load(data_file)
        data_file.close()
    print(file_path)
    print(collected_data)
    return collected_data


if __name__ == '__main__':
    main()
