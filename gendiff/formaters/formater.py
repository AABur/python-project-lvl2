# -*- coding:utf-8 -*-

from gendiff.formaters.json import format_json
from gendiff.formaters.plain import format_plain
from gendiff.formaters.stylish import format_stylish

FORMATERS = {  # noqa:WPS407
    'json': format_json,
    'plain': format_plain,
    'stylish': format_stylish,
}
DEFAULT_STYLE = 'stylish'
STYLE_ERROR_MSG = 'Output format {0} is invalid. Chose one of {1}'


class GendiffFormaterError(Exception):
    pass  # noqa: WPS420, WPS604


def call_formater(diff, style=DEFAULT_STYLE):
    style = FORMATERS.get(style)
    if style is not None:
        return style(diff)
    raise GendiffFormaterError(
        STYLE_ERROR_MSG.format(style, list(FORMATERS.keys())),
    )
