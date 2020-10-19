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

from gendiff.comparator import generate_diff
from gendiff.format_plain import print_plain, renderer
from gendiff.format_structured import render


def main():  # noqa:WPS213
    """Generate diff CLI.

    CLI usage: gendiff [-h] [-f FORMAT] first_file second_file
    """
    parser = argparse.ArgumentParser(
        description='Generate difference of two JSON or YAML files.',
    )
    parser.add_argument(
        'first_file',
        help='first file to compare',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        'second_file',
        help='second file to compare',
        type=argparse.FileType('r'),
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=('structured', 'plain', 'json'),
        default='structured',
        help='set output format',
    )
    args = parser.parse_args()
    diff = (generate_diff(args.first_file.name, args.second_file.name))
    if args.format == 'plain':
        print(print_plain(renderer(diff)))
    elif args.format == 'json':
        print(json.dumps(diff))
    else:
        print(render(diff))


if __name__ == '__main__':
    main()
