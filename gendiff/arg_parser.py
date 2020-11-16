# -*- coding:utf-8 -*-
"""argparser."""
import argparse

from gendiff.formaters import STYLES


# TODO написать тесты
def arg_parser():
    parser = argparse.ArgumentParser(
        description='Generate difference of two JSON or YAML files.',
    )
    parser.add_argument(
        'first_file',
        help='first file to compare',
    )
    parser.add_argument(
        'second_file',
        help='second file to compare',
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=(STYLES.keys()),
        default='stylish',
        help='set output format (default: stylish)',
    )
    return parser.parse_args()
