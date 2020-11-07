# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.comparator import generate_diff


@pytest.mark.parametrize(
    'style, file_before, fiel_after, file_result',
    [
        ('plain', 'simple_before_path', 'simple_after_path', 'result_simple_plain'),
        ('plain', 'complex_before_path', 'complex_after_path', 'result_complex_plain'),
        ('structured', 'simple_before_path', 'simple_after_path', 'result_simple_structured'),  # noqa:E501
        ('structured', 'complex_before_path', 'complex_after_path', 'result_complex_structured'),  # noqa:E501
        ('json', 'simple_before_path', 'simple_after_path', 'result_simple_json'),
        ('json', 'complex_before_path', 'complex_after_path', 'result_complex_json'),
    ],
)
def test_generate_diff(style, file_before, fiel_after, file_result, request):
    before = request.getfixturevalue(file_before)
    after = request.getfixturevalue(fiel_after)
    with open(request.getfixturevalue(file_result), 'r') as file:
        result = file.read()
    assert generate_diff(before, after, style) == result
