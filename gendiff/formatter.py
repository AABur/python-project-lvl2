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
    if isinstance(source, dict):
        output_items = []
        for key in source:
            source_value = source.get(key)
            status = source_value.get('status', '') if isinstance(
                source_value, dict,
            ) else ''
            new_indent = indent + INDENT_STEP
            if status == 'updated':
                output_items.append(
                    new_item(
                        key,
                        'removed',
                        source_value.get('value'),
                        new_indent,
                    ),
                )
                output_items.append(
                    new_item(
                        key,
                        'added',
                        source_value.get('updated_value'),
                        new_indent,
                    ),
                )
                continue
            elif status != '':
                output_items.append(
                    new_item(
                        key,
                        status,
                        source_value.get('value'),
                        new_indent,
                    ),
                )
                continue
            output_items.append(
                new_item(
                    key,
                    status,
                    source_value,
                    new_indent,
                ),
            )
        return '{{{}}}'.format(
            ''.join(output_items) + LF_CH + HT_CH * indent,
        )
    return source


def new_item(key, status, new_value, indent):
    """[summary].

    [extended_summary]

    Args:
        key ([type]): [description]
        status ([type]): [description]
        new_value ([type]): [description]
        indent ([type]): [description]

    Returns:
        [type]: [description]
    """
    return '{}{}{}: {}'.format(
        LF_CH + HT_CH * indent,
        get_status_sign(status),
        key,
        render(new_value, indent),
    )
