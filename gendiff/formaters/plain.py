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
    sorted_diff = sort_diff(flatten(diff))
    for diff_key, diff_value in sorted_diff.items():
        status = diff_value.get(STATUS)
        value = format_value(diff_value.get(VALUE))
        if status == ADDED:
            plain_diff.append(ADDED_STR.format(diff_key, value))
        elif status == REMOVED:
            plain_diff.append(REMOVED_STR.format(diff_key))
        elif status == UPDATED:
            updated_value = format_value(diff_value.get(UPDATED_VALUE))
            plain_diff.append(UPDATED_STR.format(
                diff_key, value, updated_value,
            ))
    return '\n'.join(plain_diff)


def sort_diff(diff):
    return dict(sorted(diff.items(), key=lambda item: item[0]))


# FIXME ! КОСТЫЛЬ - обработка случая когда 'staus' - это реальный ключ
def flatten(diff, diff_key='', result=None):
    new_result = {} if result is None else result
    status = diff.get(STATUS)
    if status and not isinstance(status, dict):  # ! КОСТЫЛЬ!!! issue test
        new_result[diff_key] = diff
        return new_result
    for next_key in diff.keys():
        new_key = '{0}.{1}'.format(diff_key, next_key) if diff_key else next_key
        flatten(diff[next_key], new_key, new_result)
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
