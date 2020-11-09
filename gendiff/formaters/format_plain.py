# -*- coding:utf-8 -*-
"""Generating plain text output."""


from gendiff.constants import (
    ADDED,
    REMOVED,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

COMPLEX_VALUE = '[complex value]'


ADDED_STR = 'Property {0} was added with value: {1}'
REMOVED_STR = 'Property {0} was removed'
UPDATED_STR = 'Property {0} was updated. From {1} to {2}'


# FIXME noqa
def generate_plain_diff(diff):
    get_pattern = {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }.get
    plain_diff = []
    for key, (status, *value) in flatt(diff).items():  # noqa: WPS414, WPS405
        if get_pattern(status):
            plain_diff.append(get_pattern(status).format(key, *value))
    return '\n'.join(plain_diff)


# FIXME noqa
def flatt(diff):  # noqa: WPS210
    flatted = {}
    for diff_key, diff_value in diff.items():
        if diff_value.get(STATUS):
            flatted[diff_key] = get_value(diff_value.get(STATUS), diff_value)
        else:
            for flatt_key, flatt_value in flatt(diff_value).items():
                complex_key = '{0}.{1}'.format(diff_key, flatt_key)
                flatted[complex_key] = flatt_value
    return flatted


def get_value(status, v1):
    if status != UPDATED:
        added_value = format_value(v1.get(VALUE))
        return (status, added_value)
    updated_from = format_value(v1.get(VALUE))
    updated_to = format_value(v1.get(UPDATED_VALUE))
    return (UPDATED, updated_from, updated_to)


def format_value(value):
    if isinstance(value, dict):
        return COMPLEX_VALUE
    if isinstance(value, bool) or value is None:
        return str(value).lower()
    if isinstance(value, str):
        return "'{0}'".format(value)
    return value
