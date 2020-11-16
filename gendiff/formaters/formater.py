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


def call_formater(diff, style):
    if style not in STYLES:
        raise Exception('Style {0} not implemented'.format(style))
    return STYLES[style](diff)


# def sort_dict(item: dict):
#     return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(item.items())}
