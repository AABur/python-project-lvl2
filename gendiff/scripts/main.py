# -*- coding:utf-8 -*-

from gendiff import generate_diff
from gendiff.arg_parser import arg_parser
from gendiff.formaters.formater import GendiffFormaterError
from gendiff.loader import GendiffFileError


def main():
    args = arg_parser().parse_args()
    try:
        print(
            generate_diff(
                args.first_file,
                args.second_file,
                args.format,
            ),
        )
    except (GendiffFileError, GendiffFormaterError) as err:
        print(err)
        exit(1)


if __name__ == '__main__':
    main()
