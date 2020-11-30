# -*- coding:utf-8 -*-
"""Generate diff.

Compares two configuration files.

CLI usage:
gendiff [-h] [-f FORMAT] first_file second_file

function usage:
from gendiff import generate_diff
diff = generate_diff(file_path1, file_path2)
"""
from gendiff import generate_diff
from gendiff.arg_parser import arg_parser


def main():
    """Generate diff CLI.

    CLI usage: gendiff [-h] [-f FORMAT] first_file second_file
    """
    args = arg_parser().parse_args()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
        ),
    )


if __name__ == '__main__':
    main()
