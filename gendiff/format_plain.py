# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""

from gendiff.common_values import (
    COMPLEX_VALUE,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)


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
            if v1.get(STATUS, ''):
                flatted[k1] = get_value(v1.get(STATUS, ''), v1)
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
