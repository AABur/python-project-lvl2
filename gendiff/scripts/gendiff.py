# -*- coding:utf-8 -*-

"""Generate diff script."""


import argparse
import json


def main():
    """Generate diff."""
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_json = json.load(args.first_file)
    second_json = json.load(args.second_file)
    difference = parse(first_json, second_json)
    print_diff(difference)


def parse(first_json, second_json):
    """parse.

    [extended_summary]

    Args:
        first_json ([type]): [description]
        second_json ([type]): [description]

    Returns:
        [type]: [description]
    """
    diff = {}
    for key1 in first_json.keys():
        diff[key1] = [first_json.get(key1), second_json.get(key1)]
    for key2 in second_json.keys():
        diff[key2] = [first_json.get(key2), second_json.get(key2)]
    return {key: diff[key] for key in sorted(diff)}


def print_diff(diff):
    """print_diff.

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
