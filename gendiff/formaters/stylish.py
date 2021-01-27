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


def format_stylish(node, indent=0):  # noqa: WPS210
    output = []
    for node_key, node_value in sorted(node.items()):
        new_indent = indent + INDENT_STEP
        status = node_value.get(STATUS)
        if status == UPDATED:
            value = format_value(node_value[VALUE], new_indent)
            output.append(create_item(new_indent, REMOVED, node_key, value))
            value = format_value(node_value[UPDATED_VALUE], new_indent)
            output.append(create_item(new_indent, ADDED, node_key, value))
            continue
        if status == NESTED:
            value = format_stylish(node_value[VALUE], new_indent)
        else:
            value = format_value(node_value[VALUE], new_indent)
        output.append(create_item(new_indent, status, node_key, value))
    return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)


def format_value(node, indent):
    if isinstance(node, dict):
        output = []
        for node_key, node_value in node.items():
            new_indent = indent + INDENT_STEP
            value = format_value(node_value, new_indent)
            output.append(create_item(new_indent, None, node_key, value))
        return '{{{0}}}'.format(''.join(output) + LF_CHAR + INDENT_CHAR * indent)  # noqa: E501
    if isinstance(node, bool):
        return str(node).lower()
    if node is None:
        return 'null'
    return str(node)


def create_item(indent, status, node_key, node_value):
    prefix = LF_CHAR + INDENT_CHAR * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(prefix, node_key, node_value)
