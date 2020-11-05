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


# FIXME noqa:WPS231, WPS210
def generate_structured_diff(source, indent=0):  # noqa:WPS231, WPS210
    if isinstance(source, dict):
        output_items = []
        new_item = ''
        for key in source:
            new_indent = indent + INDENT_STEP
            source_value = source.get(key)
            status = get_status(source_value)
            if status == UPDATED:
                output_items.append(
                    create_item(
                        key,
                        REMOVED,
                        source_value.get(VALUE),
                        new_indent,
                    ),
                )
                output_items.append(
                    create_item(
                        key,
                        ADDED,
                        source_value.get(UPDATED_VALUE),
                        new_indent,
                    ),
                )
                continue
            new_item = create_item(
                key,
                status,
                source_value,
                new_indent,
            ) if status == EMPTY else create_item(
                key,
                status,
                source_value.get(VALUE),
                new_indent,
            )
            output_items.append(new_item)
        return '{{{0}}}'.format(
            EMPTY.join(output_items) + LF_CH + HT_CH * indent,
        )
    return source


def get_status(source_value):
    return source_value.get(STATUS, EMPTY) if isinstance(
        source_value, dict,
    ) else EMPTY


def create_item(key, status, new_value, indent):
    return '{0}{1}{2}: {3}'.format(
        LF_CH + HT_CH * indent,
        get_status_sign(status),
        key,
        generate_structured_diff(new_value, indent),
    )


def get_status_sign(status):
    return {
        'added': '+ ',
        'removed': '- ',
        'unchanged': '  ',
    }.get(status, EMPTY)
