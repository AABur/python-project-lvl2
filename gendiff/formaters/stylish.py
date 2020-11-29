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


def prepare_stylish(source, indent=0):
    if isinstance(source, bool):
        return str(source).lower()
    if source is None:
        return 'null'
    if not isinstance(source, dict):
        return source
    output = ''
    for key, node in source.items():
        new_indent = indent + INDENT_STEP
        status = node.get(STATUS) if isinstance(node, dict) else None
        if status is None:
            value = prepare_stylish(node, new_indent)
        else:
            value = prepare_stylish(node.get(VALUE), new_indent)
            updated_value = prepare_stylish(node.get(UPDATED_VALUE), new_indent)
        if status == UPDATED:
            output += create_item(new_indent, REMOVED, key, value)
            output += create_item(new_indent, ADDED, key, updated_value)
            continue
        output += create_item(new_indent, status, key, value)
    return '{{{0}}}'.format(output + LF_CH + HT_CH * indent)


def create_item(indent, status, key, *prep_val):
    prefix = create_prefix(status, indent)
    result = '{0}{1}: {2}'.format(prefix, key, prep_val[0])
    return result


def create_prefix(status, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = {
        ADDED: '+ ',
        REMOVED: '- ',
    }.get(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return prefix
