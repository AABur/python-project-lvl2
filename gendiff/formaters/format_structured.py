# -*- coding:utf-8 -*-
"""Generating structured text output."""

from gendiff.constants import (
    ADDED,
    REMOVED,
    STATUS,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

LF_CH = '\n'
HT_CH = ' '
INDENT_STEP = 4
EMPTY = ''


def get_status_sign(status):
    return {
        'added': '+ ',
        'removed': '- ',
        'unchanged': '  ',
        'updated': '+-',
    }.get(status, EMPTY)


# FIXME noqa:WPS231
def render(source, indent=0):  # noqa:WPS231
    if isinstance(source, dict):
        output_items = []
        for key in source:
            new_indent = indent + INDENT_STEP
            source_value = source.get(key)
            status = source_value.get(STATUS, EMPTY) if isinstance(
                source_value, dict,
            ) else EMPTY
            if status == UPDATED:
                output_items.append(
                    new_item(
                        key,
                        REMOVED,
                        source_value.get(VALUE),
                        new_indent,
                    ),
                )
                output_items.append(
                    new_item(
                        key,
                        ADDED,
                        source_value.get(UPDATED_VALUE),
                        new_indent,
                    ),
                )
            elif status == EMPTY:
                output_items.append(
                    new_item(
                        key,
                        status,
                        source_value,
                        new_indent,
                    ),
                )
            else:
                output_items.append(
                    new_item(
                        key,
                        status,
                        source_value.get(VALUE),
                        new_indent,
                    ),
                )
        return '{{{0}}}'.format(
            EMPTY.join(output_items) + LF_CH + HT_CH * indent,
        )
    return source


def new_item(key, status, new_value, indent):
    return '{0}{1}{2}: {3}'.format(
        LF_CH + HT_CH * indent,
        get_status_sign(status),
        key,
        render(new_value, indent),
    )
