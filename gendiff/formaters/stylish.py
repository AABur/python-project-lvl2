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


get_status_sign = {
    ADDED: '+ ',
    REMOVED: '- ',
}.get


def format_stylish(source):
    sorted_source = sort_dict(source)
    return prepare_stylish(sorted_source)


def sort_dict(item):
    result = {}
    for key, value in sorted(item.items()):
        is_sort = isinstance(value, dict) and not value.get(STATUS)
        if is_sort:
            result[key] = sort_dict(value)
        else:
            result[key] = value
    return result


def prepare_stylish(source, indent=0):  # noqa: WPS210
    if not isinstance(source, dict):
        return format_simple_value(source)
    output = []
    for key, node in source.items():
        new_indent = indent + INDENT_STEP
        status = node.get(STATUS) if isinstance(node, dict) else None
        if status == UPDATED:
            value = prepare_stylish(node.get(VALUE), new_indent)
            output.append(create_item(new_indent, REMOVED, key, value))
            value = prepare_stylish(node.get(UPDATED_VALUE), new_indent)
            output.append(create_item(new_indent, ADDED, key, value))
            continue
        if status is None:
            value = prepare_stylish(node, new_indent)
        else:
            value = prepare_stylish(node.get(VALUE), new_indent)
        output.append(create_item(new_indent, status, key, value))
    return '{{{0}}}'.format(''.join(output) + LF_CH + HT_CH * indent)


def format_simple_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def create_item(indent, status, key, prep_val):
    prefix = create_prefix(status, indent)
    return '{0}{1}: {2}'.format(prefix, key, prep_val)


def create_prefix(status, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return prefix
