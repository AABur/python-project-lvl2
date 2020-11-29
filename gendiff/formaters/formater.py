# -*- coding:utf-8 -*-
"""Generating plain text output."""

from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish

STYLES = {  # noqa:WPS407
    'json': format_json,
    'plain': format_plain,
    'stylish': format_stylish,
}
DEFAULT_STYLE = 'stylish'


def call_formater(diff, style=DEFAULT_STYLE):
    return STYLES.get(style)(diff)
