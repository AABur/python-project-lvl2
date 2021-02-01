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

COMPLEX_VALUE = '[complex value]'

ADDED_STR = "Property '{0}' was added with value: {1}"
REMOVED_STR = "Property '{0}' was removed"
UPDATED_STR = "Property '{0}' was updated. From {1} to {2}"


def format_plain(diff):  # noqa:WPS210
    plain_diff = []
    for diff_key, diff_value in sorted(flatten(diff).items()):
        status = diff_value[STATUS]
        value = format_value(diff_value[VALUE])
        if status == ADDED:
            plain_diff.append(ADDED_STR.format(diff_key, value))
        elif status == REMOVED:
            plain_diff.append(REMOVED_STR.format(diff_key))
        elif status == UPDATED:
            updated_value = format_value(diff_value[UPDATED_VALUE])
            plain_diff.append(UPDATED_STR.format(
                diff_key, value, updated_value,
            ))
    return '\n'.join(plain_diff)


def flatten(node, prefix='', flatt=None):
    flatted_node = {} if flatt is None else flatt
    for node_key, node_value in node.items():
        new_key = '{0}.{1}'.format(prefix, node_key) if prefix else node_key
        if node_value[STATUS] == NESTED:
            flatten(node_value[VALUE], new_key, flatted_node)
        else:
            flatted_node[new_key] = node_value
    return flatted_node


def format_value(value):
    if isinstance(value, dict):
        return COMPLEX_VALUE
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'{0}'".format(value)
    return str(value)
