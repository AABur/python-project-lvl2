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
    plain_diff = []
    # FIXME noqa
    for key, (status, *value) in flat_diff(diff).items():  # noqa: WPS414, WPS405, E501
        if patterns.get(status):
            plain_diff.append(patterns.get(status).format(key, *value))
    return '\n'.join(plain_diff)


def flat_diff(diff):
    flatted = {}
    for k1, v1 in diff.items():
        if v1.get(STATUS):
            flatted[k1] = get_value(v1.get(STATUS), v1)
        else:
            for k2, v2 in flat_diff(v1).items():
                flatted['{0}.{1}'.format(k1, k2)] = v2
    return flatted


# FIXME separate: getting value and masking COMPLEX
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
