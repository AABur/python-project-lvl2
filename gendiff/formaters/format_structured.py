# -*- coding:utf-8 -*-
"""Generating structured text output."""

from gendiff.constants import (
    ADDED,
    REMOVED,
    STATUS,
    UNCHANGED,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)

LF_CH = '\n'
HT_CH = ' '
INDENT_STEP = 4
EMPTY = ''


def generate_structured_diff(source, indent=0):
    if isinstance(source, dict):
        output_items = []
        for key in source:
            source_value = source.get(key)
            status = get_status(source_value)
            if status == UPDATED:
                output_items.extend(get_updated(
                    key,
                    source_value,
                    indent + INDENT_STEP,
                ))
                continue
            value = source_value if status == EMPTY else source_value.get(VALUE)
            output_items.extend(create_item(
                key,
                status,
                value,
                indent + INDENT_STEP,
            ))
        return '{{{0}}}'.format(
            EMPTY.join(output_items) + LF_CH + HT_CH * indent,
        )
    return format_value(source)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_updated(key, source_value, new_indent):
    item_before = create_item(
        key,
        REMOVED,
        source_value.get(VALUE),
        new_indent,
    )
    item_after = create_item(
        key,
        ADDED,
        source_value.get(UPDATED_VALUE),
        new_indent,
    )
    return item_before, item_after


def get_status(source_value):
    return source_value.get(STATUS, EMPTY) if isinstance(
        source_value, dict,
    ) else EMPTY


def create_item(key, status, new_value, indent):
    get_status_sign = {
        ADDED: '+ ',
        REMOVED: '- ',
        UNCHANGED: '  ',
    }.get(status)
    if not get_status_sign:
        get_status_sign = EMPTY
    return '{0}{1}{2}: {3}'.format(
        LF_CH + HT_CH * indent,
        get_status_sign,
        key,
        generate_structured_diff(new_value, indent),
    )
