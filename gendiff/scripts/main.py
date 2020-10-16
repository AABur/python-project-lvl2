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

from gendiff.comparator import generate_diff
from gendiff.format_json import render
from gendiff.formatt_plane import flatten


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
    print('-----------')
    print(flatten(diff))


if __name__ == '__main__':
    main()
