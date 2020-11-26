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


def prepare_plain(diff):  # noqa: WPS210
    get_pattern = {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }.get
    plain_diff = []
    sorted_diff = sort_diff(flatt(diff))
    for key, value in sorted_diff.items():
        pattern = get_pattern(value.get(STATUS))
        if pattern:
            values = (
                format_value(value.get(VALUE)),
                format_value(value.get(UPDATED_VALUE)),
            )
            plain_diff.append(pattern.format(key, *values))
    return '\n'.join(plain_diff)


def sort_diff(diff):
    return dict(sorted(diff.items(), key=lambda item: item[0]))


def flatt(nest):  # noqa: WPS210
    flatted = {}
    for nest_key, nest_value in nest.items():
        if nest_value.get(STATUS):
            flatted[nest_key] = nest_value
        else:
            for child_key, child_value in flatt(nest_value).items():
                flatted_key = '{0}.{1}'.format(nest_key, child_key)
                flatted[flatted_key] = child_value
    return flatted


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
