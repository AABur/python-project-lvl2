# -*- coding:utf-8 -*-

from gendiff.comparator import compose_diff
from gendiff.formaters import DEFAULT_STYLE, call_formater
from gendiff.loader import collect_data


def generate_diff(first_file, second_file, output_format=DEFAULT_STYLE):
    first_data = collect_data(first_file)
    second_data = collect_data(second_file)
    diff = compose_diff(first_data, second_data)
    return call_formater(diff, output_format)
