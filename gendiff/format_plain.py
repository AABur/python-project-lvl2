# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""

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
EMPTY_STR = ''


def print_plain(source):  # noqa:WPS231
    """[summary].

    [extended_summary]

    Args:
        source ([type]): [description]

    Returns:
        [type]: [description]
    """
    plain = EMPTY_STR
    str_str = EMPTY_STR
    for k1, v1 in source.items():
        if v1[0] == ADDED:
            str_str = ADDED_STR.format(k1, v1[1])
        elif v1[0] == REMOVED:
            str_str = REMOVED_STR.format(k1)
        elif v1[0] == UPDATED:
            str_str = UPDATED_STR.format(k1, v1[1], v1[2])
        else:
            continue
        plain = ' '.join([plain, str_str, '\n'])
    return plain


def renderer(source):
    """[summary].

    [extended_summary]

    Args:
        source ([type]): [description]

    Returns:
        [type]: [description]
    """
    flatted = {}
    for k1, v1 in source.items():
        if isinstance(v1, dict):
            if v1.get(STATUS, EMPTY_STR):
                flatted[k1] = get_value(v1.get(STATUS, EMPTY_STR), v1)
            else:
                for k2, v2 in renderer(v1).items():
                    flatted['{0}.{1}'.format(k1, k2)] = v2
        else:
            flatted[k1] = v1
    return flatted


def get_value(status, v1):
    """[summary].

    [extended_summary]

    Args:
        status ([type]): [description]
        v1 ([type]): [description]

    Returns:
        [type]: [description]
    """
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
