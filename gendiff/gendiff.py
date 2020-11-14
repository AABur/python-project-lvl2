# -*- coding:utf-8 -*-
"""Calculate difference."""

from gendiff.comparator import compile_diff
from gendiff.formaters import call_formater
from gendiff.loader import collect_data


def generate_diff(old_file_path, new_file_path, output_format='stylish'):
    old = collect_data(old_file_path)
    new = collect_data(new_file_path)
    diff = compile_diff(old, new)
    return call_formater(diff, output_format)
