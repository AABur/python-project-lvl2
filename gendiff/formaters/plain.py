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


def format_plain(diff):  # noqa:WPS210
    plain_diff = []
    sorted_diff = _sort_diff(flatten(diff))
    for diff_key, diff_value in sorted_diff.items():
        pattern = _get_pattern()(diff_value.get(STATUS))
        if pattern:
            values = (
                format_value(diff_value.get(VALUE)),
                format_value(diff_value.get(UPDATED_VALUE)),
            )
            plain_diff.append(pattern.format(diff_key, *values))
    return '\n'.join(plain_diff)


def _get_pattern():
    return {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }.get


def _sort_diff(diff):
    return dict(sorted(diff.items(), key=lambda item: item[0]))


def flatten(nest, key='', result=None):
    new_result = {} if result is None else result
    if nest.get(STATUS):
        new_result[key] = nest
        return new_result
    for next_key in nest.keys():
        new_key = '{0}.{1}'.format(key, next_key) if key else next_key
        flatten(nest[next_key], new_key, new_result)
    return new_result


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
