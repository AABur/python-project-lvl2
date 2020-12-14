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


def format_stylish(diff):
    sorted_diff = sort_dict(diff)
    return prepare_stylish(sorted_diff)


# FIXME ! КОСТЫЛЬ - обработка случая когда 'staus' - это реальный ключ
def sort_dict(node):
    sorted_dict = {}
    for node_key, node_value in sorted(node.items()):
        status = node_value.get(STATUS)
        if isinstance(status, dict):  # ! КОСТЫЛЬ!!!
            status = None
        is_sort = isinstance(node_value, dict) and not status
        if is_sort:
            sorted_dict[node_key] = sort_dict(node_value)
        else:
            sorted_dict[node_key] = node_value
    return sorted_dict


# FIXME ! КОСТЫЛЬ - обработка случая когда 'staus' - это реальный ключ
def prepare_stylish(node, indent=0):  # noqa: WPS210 WPS231
    if not isinstance(node, dict):
        return format_simple_value(node)
    output = []
    for node_key, node_value in node.items():
        new_indent = indent + INDENT_STEP
        status = node_value.get(STATUS) if isinstance(node_value, dict) else None  # noqa:E501
        if isinstance(status, dict):  # ! КОСТЫЛЬ!!!
            status = None
        if status == UPDATED:
            value = prepare_stylish(node_value.get(VALUE), new_indent)
            output.append(create_item(new_indent, REMOVED, node_key, value))
            value = prepare_stylish(node_value.get(UPDATED_VALUE), new_indent)
            output.append(create_item(new_indent, ADDED, node_key, value))
            continue
        if status is None:
            value = prepare_stylish(node_value, new_indent)
        else:
            value = prepare_stylish(node_value.get(VALUE), new_indent)
        output.append(create_item(new_indent, status, node_key, value))
    return '{{{0}}}'.format(''.join(output) + LF_CH + HT_CH * indent)


def format_simple_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def create_item(indent, status, key, value):
    prefix = create_prefix(status, indent)
    return '{0}{1}: {2}'.format(prefix, key, value)


def create_prefix(status, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return prefix
