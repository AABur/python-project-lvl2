# -*- coding:utf-8 -*-

"""Formatters."""

from gendiff.formaters.format_json import generate_json_diff
from gendiff.formaters.format_plain import generate_plain_diff
from gendiff.formaters.format_stylish import generate_stylish_diff

__all__ = (  # noqa:WPS410
    'generate_json_diff',
    'generate_plain_diff',
    'generate_stylish_diff',
)
