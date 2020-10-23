# -*- coding:utf-8 -*-
"""Generating plain text otput."""

from gendiff.common_values import (
    ADDED,
    COMPLEX_VALUE,
    REMOVED,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

ADDED_STR = 'Property {0} was added with value: {1}'
REMOVED_STR = 'Property {0} was removed'
UPDATED_STR = 'Property {0} was updated. From {1} to {2}'


def print_plain(source):  # noqa:WPS210
    patterns = {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }
    plain = ''
    rendered_val = renderer(source)
    for key, key_value in rendered_val.items():
        status = key_value[0]
        if status not in patterns.keys():
            continue
        plain = ' '.join(
            [
                plain,
                patterns[status].format(key, *key_value[1:]),
                '\n',
            ],
        )
    return plain


def renderer(source):
    flatted = {}
    for k1, v1 in source.items():
        if v1.get(STATUS):
            flatted[k1] = get_value(v1.get(STATUS), v1)
        else:
            for k2, v2 in renderer(v1).items():
                flatted['{0}.{1}'.format(k1, k2)] = v2
    return flatted


def get_value(status, v1):
    if status != UPDATED:
        added_value = COMPLEX_VALUE if isinstance(
            v1.get(VALUE), dict,
        ) else v1.get(VALUE)
        return (status, repr(added_value))
    updated_from = COMPLEX_VALUE if isinstance(
        v1.get(VALUE), dict,
    ) else v1.get(VALUE)
    updated_to = COMPLEX_VALUE if isinstance(
        v1.get(UPDATED_VALUE), dict,
    ) else v1.get(UPDATED_VALUE)
    return (UPDATED, repr(updated_from), repr(updated_to))
