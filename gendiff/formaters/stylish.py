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


def prepare_stylish(source, indent=0):  # noqa: WPS210, WPS231
    if isinstance(source, bool):
        return str(source).lower()
    if source is None:
        return 'null'
    if not isinstance(source, dict):
        return source
    output = ''
    for key, node in source.items():
        status = node.get(STATUS) if isinstance(node, dict) else None
        new_indent = indent + INDENT_STEP
        value = node.get(VALUE) if status else node
        if status == UPDATED:
            updated_value = node.get(UPDATED_VALUE) if status else node
            output += create_item(key, REMOVED, value, new_indent)
            output += create_item(key, ADDED, updated_value, new_indent)
            continue
        output += create_item(key, status, value, new_indent)
    return '{{{0}}}'.format(output + LF_CH + HT_CH * indent)


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
