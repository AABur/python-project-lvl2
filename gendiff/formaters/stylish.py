# -*- coding:utf-8 -*-
"""Generating stylish text output."""

from gendiff.comparator import (
    ADDED,
    REMOVED,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

LF_CH = '\n'
HT_CH = ' '
INDENT_STEP = 4


def prepare_stylish(source, indent=0):  # noqa:WPS210
    if isinstance(source, bool):
        return str(source).lower()
    if source is None:
        return 'null'
    if not isinstance(source, dict):
        return source
    output_items = []
    for key, value in source.items():
        status = value.get(STATUS) if isinstance(value, dict) else None
        new_indent = indent + INDENT_STEP
        if status == UPDATED:
            output_items.extend(get_updated(key, value, new_indent))
            continue
        new_value = value.get(VALUE) if status else value
        output_items.extend(create_item(key, status, new_value, new_indent))
    return '{{{0}}}'.format(''.join(output_items) + LF_CH + HT_CH * indent)


def get_updated(key, source, indent):
    item_before = create_item(key, REMOVED, source.get(VALUE), indent)
    item_after = create_item(key, ADDED, source.get(UPDATED_VALUE), indent)
    return item_before, item_after


def create_item(key, status, value, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, key, prepare_stylish(value, indent))


def get_status_sign(status):
    return {
        ADDED: '+ ',
        REMOVED: '- ',
    }.get(status)
