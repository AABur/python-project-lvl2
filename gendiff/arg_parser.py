# -*- coding:utf-8 -*-

import argparse

from gendiff.formaters import DEFAULT_STYLE, FORMATERS


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Generate difference of two JSON or YAML files.',
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='first file to compare',
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='second file to compare',
    )
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=(FORMATERS.keys()),
        default=DEFAULT_STYLE,
        help="set output format (default: '{0}')".format(DEFAULT_STYLE),
    )
    return parser
