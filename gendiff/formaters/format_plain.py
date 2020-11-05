# -*- coding:utf-8 -*-
"""Generating plain text output."""

from gendiff.constants import (
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


def generate_plain_diff(diff):
    patterns = {
        ADDED: ADDED_STR,
        REMOVED: REMOVED_STR,
        UPDATED: UPDATED_STR,
    }
    plain = ''
    rendered_val = parse_diff(diff)
    for key, key_value in rendered_val.items():
        if key_value[0] in patterns.keys():
            plain = ' '.join(
                [
                    plain,
                    patterns[key_value[0]].format(key, *key_value[1:]),
                    '\n',
                ],
            )
    return plain


def parse_diff(diff):
    flatted = {}
    for k1, v1 in diff.items():
        if v1.get(STATUS):
            flatted[k1] = get_value(v1.get(STATUS), v1)
        else:
            for k2, v2 in parse_diff(v1).items():
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
