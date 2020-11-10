# -*- coding:utf-8 -*-
"""Generating plain text output."""


from gendiff.formaters.format_json import prepare_json
from gendiff.formaters.format_plain import prepare_plain
from gendiff.formaters.format_stylish import prepare_stylish


def call_formater(diff, style):
    if style == 'plain':
        return prepare_plain(diff)
    elif style == 'json':
        return prepare_json(diff)
    return prepare_stylish(diff)
