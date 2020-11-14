# -*- coding:utf-8 -*-
"""Calculate difference."""

STATUS = 'status'

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

VALUE = 'value'
UPDATED_VALUE = 'updated_value'


def compile_diff(old, new):
    compared = {}
    keys = {
        'keys_union': sorted(old.keys() | new.keys()),
        'keys_removed': old.keys() - new.keys(),
        'keys_intersection': old.keys() & new.keys(),
    }
    for key in keys['keys_union']:
        old_value = old.get(key)
        new_value = new.get(key)
        if key in keys['keys_intersection']:
            compared[key] = compare_same_keys(old_value, new_value)
            continue
        compared[key] = {
            STATUS: REMOVED,
            VALUE: old_value,
        } if key in keys['keys_removed'] else {
            STATUS: ADDED,
            VALUE: new_value,
        }
    return compared


def compare_same_keys(old_value, new_value):
    if old_value == new_value:
        return {
            STATUS: UNCHANGED,
            VALUE: old_value,
        }
    elif isinstance(old_value, dict) and isinstance(new_value, dict):
        return compile_diff(old_value, new_value)
    return {
        STATUS: UPDATED,
        VALUE: old_value,
        UPDATED_VALUE: new_value,
    }
