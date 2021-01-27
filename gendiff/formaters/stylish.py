# -*- coding:utf-8 -*-

from gendiff.comparator import (
    ADDED,
    NESTED,
    REMOVED,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

LF_CHAR = '\n'
INDENT_CHAR = ' '
INDENT_STEP = 4


get_status_sign = {
    ADDED: '+ ',
    REMOVED: '- ',
}.get


def format_stylish(diff):
    return prepare_stylish(sort_diff(diff))


# FIXME
def prepare_stylish(node, indent=0):  # noqa: WPS210
    output = []
    for node_key, node_value in node.items():
        new_indent = indent + INDENT_STEP
        status = node_value.get(STATUS)
        if status == UPDATED:
            value = format_value(node_value[VALUE], new_indent)
            output.append(create_item(new_indent, REMOVED, node_key, value))
            value = format_value(node_value[UPDATED_VALUE], new_indent)
            output.append(create_item(new_indent, ADDED, node_key, value))
            continue
        if status == NESTED:
            value = prepare_stylish(node_value[VALUE], new_indent)
        else:
            value = format_value(node_value[VALUE], new_indent)
        output.append(create_item(new_indent, status, node_key, value))
    return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)


def format_value(value, indent):
    if isinstance(value, dict):
        return format_dict(value, indent)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_dict(node, indent=0):  # noqa: WPS210
    output = []
    for node_key, node_value in node.items():
        new_indent = indent + INDENT_STEP
        status = node_value.get(STATUS) if isinstance(node_value, dict) else None  # noqa: E501
        if status is None:
            value = format_value(node_value, new_indent)
        else:
            value = format_value(node_value[VALUE], new_indent)
        output.append(create_item(new_indent, status, node_key, value))
    return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)


def create_item(indent, status, node_key, node_value):
    prefix = create_prefix(status, indent)
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)


def create_prefix(status, indent):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return prefix


def sort_diff(node):
    sorted_diff = {}
    for node_key, node_value in sorted(node.items()):
        status = node_value[STATUS]
        if status == NESTED:
            sorted_diff[node_key] = {
                STATUS: NESTED,
                VALUE: sort_diff(node_value[VALUE]),
            }
        else:
            sorted_diff[node_key] = node_value
    return sorted_diff
