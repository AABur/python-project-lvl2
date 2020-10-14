# -*- coding:utf-8 -*-
"""[summary].

[extended_summary]
"""
LF_CH = '\n'
HT_CH = ' '
INDENT_STEP = 4


def get_status_sign(status):
    """[summary].

    [extended_summary]

    Args:
        status ([type]): [description]

    Returns:
        [type]: [description]
    """
    return {
        'added': '+ ',
        'removed': '- ',
        'unchanged': '  ',
        'updated': '+-',
    }.get(status, '')


def render(source, indent=0):
    """[summary].

    [extended_summary]

    Args:
        source ([type]): [description]
        indent (int, optional): [description]. Defaults to 0.

    Returns:
        [type]: [description]
    """
    nl_ch = LF_CH + HT_CH * (indent + INDENT_STEP)
    if isinstance(source, dict):
        output_items = []
        for key in source:
            output_value = source.get(key)
            status = output_value.get('status', '') if isinstance(
                output_value, dict,
            ) else ''
            if status:
                output_value = output_value.get('value')
            output_items.append(
                '{}{}{}: {}'.format(
                    nl_ch,
                    get_status_sign(status),
                    key,
                    render(output_value, indent + INDENT_STEP),
                ),
            )
        return '{{{}}}'.format(
            ''.join(output_items) + LF_CH + HT_CH * indent,
        )
    return source


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
            if not v1:
                flatted[k1] = ''
            for k2, v2 in flatten(v1).items():
                flatted['{0}/{1}'.format(k1, k2)] = v2
        else:
            flatted[k1] = v1
    return flatted
