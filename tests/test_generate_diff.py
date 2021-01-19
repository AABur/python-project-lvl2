# -*- coding:utf-8 -*-

import pytest

from gendiff import generate_diff


@pytest.mark.parametrize(
    'style, file_before, file_after, file_result',
    [
        ('plain', 'simple_before_path', 'simple_after_path', 'result_simple_plain'),  # noqa:E501
        ('plain', 'complex_before_path', 'complex_after_path', 'result_complex_plain'),  # noqa:E501
        ('stylish', 'simple_before_path', 'simple_after_path', 'result_simple_stylish'),  # noqa:E501
        ('stylish', 'complex_before_path', 'complex_after_path', 'result_complex_stylish'),  # noqa:E501
    ],
)
def test_generate_diff(style, file_before, file_after, file_result, request):
    before = request.getfixturevalue(file_before)
    after = request.getfixturevalue(file_after)
    with open(request.getfixturevalue(file_result), 'r') as file:
        result = file.read()
    assert generate_diff(before, after, style) == result
