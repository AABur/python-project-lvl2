# -*- coding:utf-8 -*-
"""Test plain format generator."""

from gendiff.formaters.format_plain import print_plain


def test_print_plain_simple(simple_data, simple_result_p):
    assert print_plain(simple_data) == simple_result_p


def test_print_plain_complex(complex_data, complex_result_p):
    assert print_plain(complex_data) == complex_result_p
