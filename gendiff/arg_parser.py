# -*- coding:utf-8 -*-
"""argparser."""
import argparse


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
        choices=('structured', 'plain', 'json'),
        default='structured',
        help='set output format (default: structured)',
    )
    args = parser.parse_args()
    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        'format': args.format,
    }
