# -*- coding:utf-8 -*-

"""Generate diff script."""


import argparse


def main():
    """Generate diff."""
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
