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
    keys_union = sorted(old.keys() | new.keys())
    keys_removed = old.keys() - new.keys()
    # keys_added = new.keys() - old.keys() # noqa:E800
    keys_intersection = old.keys() & new.keys()
    for key in keys_union:
        if key in keys_intersection:
            compared[key] = _compare_same_keys(old.get(key), new.get(key))
        elif key in keys_removed:
            compared[key] = {STATUS: REMOVED, VALUE: old.get(key)}
        else:  # key in keys_added
            compared[key] = {STATUS: ADDED, VALUE: new.get(key)}
    return compared


def _compare_same_keys(old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return compile_diff(old_value, new_value)
    if old_value == new_value:
        return {STATUS: UNCHANGED, VALUE: old_value}
    return {STATUS: UPDATED, VALUE: old_value, UPDATED_VALUE: new_value}
