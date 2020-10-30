# -*- coding:utf-8 -*-
"""Test plain format generator."""

from gendiff.formaters.format_structured import render


def test_print_structured_s(simple_data, simple_result_s):
    assert render(simple_data) == simple_result_s


def test_print_structured_c(complex_data, complex_result_s):
    assert render(complex_data) == complex_result_s
