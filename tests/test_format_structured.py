# -*- coding:utf-8 -*-
"""Test plain format generator."""

import pytest

from gendiff.formaters.format_structured import render


@pytest.mark.parametrize(
    'test_data, test_result',
    [
        ('simple_data', 'simple_result_s'),
        ('complex_data', 'complex_result_s'),
    ],
)
def test_print_structured(test_data, test_result, request):
    t_data = request.getfixturevalue(test_data)
    t_result = request.getfixturevalue(test_result)
    assert render(t_data) == t_result
