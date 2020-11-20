# -*- coding:utf-8 -*-
"""Generating stylish text output."""

from gendiff.comparator import (
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


def prepare_stylish(source, indent=0):
    if isinstance(source, bool):
        return str(source).lower()
    if source is None:
        return 'null'
    if not isinstance(source, dict):
        return source
    output_items = []
    for key, value in source.items():
        status = value.get(STATUS) if isinstance(value, dict) else None
        if status == UPDATED:
            output_items.extend(get_updated(
                key,
                value,
                indent + INDENT_STEP,
            ))
            continue
        output_items.extend(create_item(
            key,
            status,
            value.get(VALUE) if status else value,
            indent + INDENT_STEP,
        ))
    return '{{{0}}}'.format(
        ''.join(output_items) + LF_CH + HT_CH * indent,
    )


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


def create_item(key, status, new_value, indent):
    prefix = LF_CH + HT_CH * indent
    status_sign = get_status_sign(status)
    if status_sign:
        prefix = prefix[:-2] + status_sign
    return '{0}{1}: {2}'.format(
        prefix,
        key,
        prepare_stylish(new_value, indent),
    )


def get_status_sign(status):
    return {
        ADDED: '+ ',
        REMOVED: '- ',
    }.get(status)
