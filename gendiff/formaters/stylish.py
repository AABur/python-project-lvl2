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
    output = ''
    for key, node in source.items():
        new_indent = indent + INDENT_STEP
        values = []
        status = node.get(STATUS) if isinstance(node, dict) else None
        if status is None:
            values.append(prepare_stylish(node, new_indent))
        else:
            values.append(prepare_stylish(node.get(VALUE), new_indent))
            values.append(prepare_stylish(node.get(UPDATED_VALUE), new_indent))
        output += create_item(new_indent, status, key, values)
    return '{{{0}}}'.format(output + LF_CH + HT_CH * indent)


def create_item(indent, status, key, prep_val):
    if status == UPDATED:
        prefix = create_prefix(REMOVED, indent)
        result = '{0}{1}: {2}'.format(prefix, key, prep_val[0])
        prefix = create_prefix(ADDED, indent)
        result += '{0}{1}: {2}'.format(prefix, key, prep_val[1])
        return result
    prefix = create_prefix(status, indent)
    return '{0}{1}: {2}'.format(prefix, key, prep_val[0])


def create_prefix(status, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = {
        ADDED: '+ ',
        REMOVED: '- ',
    }.get(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return prefix
