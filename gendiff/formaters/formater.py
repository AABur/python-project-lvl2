# -*- coding:utf-8 -*-
"""Generating plain text output."""

from gendiff.formaters.json import prepare_json
from gendiff.formaters.plain import prepare_plain
from gendiff.formaters.stylish import prepare_stylish

STYLES = {  # noqa:WPS407
    'json': prepare_json,
    'plain': prepare_plain,
    'stylish': prepare_stylish,
}
DEFAULT_STYLE = 'stylish'

# TODO добавить проверку на правильный стиль


def call_formater(diff, style=DEFAULT_STYLE):
    return STYLES.get(style)(diff)
