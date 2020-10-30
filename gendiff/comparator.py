# -*- coding:utf-8 -*-
"""Calculate differnce."""

import json

from gendiff.constants import (
    ADDED,
    REMOVED,
    STATUS,
    UNCHANGED,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)
from gendiff.formaters.format_plain import print_plain
from gendiff.formaters.format_structured import render
from gendiff.loader import collect_data


# TODO Функция generate_diff должна возвращать уже отформатированную строку
def generate_diff(old_file_path, new_file_path, output_format):
    old = collect_data(old_file_path)
    new = collect_data(new_file_path)
    diff = compare(old, new)
    if output_format == 'plain':
        return print_plain(diff)
    elif output_format == 'json':
        return json.dumps(diff)
    return render(diff)


def compare(old, new):
    compared = {}
    keys = {
        'keys_union': sorted(old.keys() | new.keys()),
        'keys_removed': old.keys() - new.keys(),
        'keys_added': new.keys() - old.keys(),
        'keys_intersection': old.keys() & new.keys(),
    }
    for key in keys['keys_union']:
        old_value = old.get(key)
        new_value = new.get(key)
        if key in keys['keys_removed']:
            compared[key] = {
                STATUS: REMOVED,
                VALUE: old_value,
            }
        if key in keys['keys_added']:
            compared[key] = {
                STATUS: ADDED,
                VALUE: new_value,
            }
        if key in keys['keys_intersection']:
            compared[key] = compare_same_keys(old_value, new_value)
    return compared


def compare_same_keys(old_value, new_value):
    if old_value == new_value:
        return {
            STATUS: UNCHANGED,
            VALUE: old_value,
        }
    elif isinstance(old_value, dict) and isinstance(new_value, dict):
        return compare(old_value, new_value)
    return {
        STATUS: UPDATED,
        VALUE: old_value,
        UPDATED_VALUE: new_value,
    }
