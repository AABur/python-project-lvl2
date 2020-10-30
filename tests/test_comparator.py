# -*- coding:utf-8 -*-
"""Generate diff tests."""

from gendiff.comparator import generate_diff


def test_generate_diff(complex1_json, complex2_json, result_data):
    assert generate_diff(
        complex1_json,
        complex2_json,
        'structured',
    ) == result_data
