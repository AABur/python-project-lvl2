# -*- coding:utf-8 -*-
"""Generating plain text output."""


from gendiff.comparator import (
    ADDED,
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


# FIXME noqa
def prepare_plain(diff):
    get_pattern = {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }.get
    plain_diff = []
    flatt_diff = flatt(diff)
    sorted_diff = sort_diff(flatt_diff)
    for key, value in sorted_diff.items():
        pattern = get_pattern(value.get(STATUS))
        if pattern:
            vvv = (format_value(value.get(VALUE)),
                   format_value(value.get(UPDATED_VALUE)))
            plain_diff.append(pattern.format(key, *vvv))
    return '\n'.join(plain_diff)


def sort_diff(diff):
    return diff


def flatt(diff):
    flatted = {}
    for diff_key, diff_value in diff.items():
        if diff_value.get(STATUS):
            flatted[diff_key] = diff_value
        else:
            for flatt_key, flatt_value in flatt(diff_value).items():
                flatted[create_key(diff_key, flatt_key)] = flatt_value
    return flatted


def create_key(diff_key, flatt_key):
    return '{0}.{1}'.format(diff_key, flatt_key)


def get_value(status, node):
    if status != UPDATED:
        added_value = format_value(node.get(VALUE))
        return (status, added_value)
    updated_from = format_value(node.get(VALUE))
    updated_to = format_value(node.get(UPDATED_VALUE))
    return (UPDATED, updated_from, updated_to)


def format_value(value):
    if isinstance(value, dict):
        return COMPLEX_VALUE
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return "'{0}'".format(value)
    return value
