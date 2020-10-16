# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""


def flatten(nested):
    """[summary].

    [extended_summary]

    Args:
        nested (dict): [description]

    Returns:
        (dict): [description]
    """
    flatted = {}
    for k1, v1 in nested.items():
        if isinstance(v1, dict):
            if v1.get('status', ''):
                flatted[k1] = get_value(v1.get('status', ''), v1)
            else:
                for k2, v2 in flatten(v1).items():
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
    if status != 'updated':
        added_value = '[complex value]' if isinstance(
            v1.get('value'), dict,
        ) else v1.get('value')
        return (status, repr(added_value))
    updated_from = '[complex value]' if isinstance(
        v1.get('value'), dict,
    ) else v1.get('value')
    updated_to = '[complex value]' if isinstance(
        v1.get('updated_value'), dict,
    ) else v1.get('updated_value')
    return ('updated', repr(updated_from), repr(updated_to))
