# -*- coding:utf-8 -*-
"""Calculate differnce."""

from gendiff.common_values import (
    ADDED,
    REMOVED,
    STATUS,
    UNCHANGED,
    UPDATED,
    UPDATED_VALUE,
    VALUE,
)
from gendiff.loader import collect_data


def generate_diff(old_file_path, new_file_path):
    old = collect_data(old_file_path)
    new = collect_data(new_file_path)
    return compare(old, new)


def compare(old, new):
    compared = {}
    compared_value = {}
    for key in sorted(old.keys() | new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        if key in old.keys() - new.keys():
            compared_value = {
                STATUS: REMOVED,
                VALUE: old_value,
            }
        if key in new.keys() - old.keys():
            compared_value = {
                STATUS: ADDED,
                VALUE: new_value,
            }
        if key in old.keys() & new.keys():
            compared_value = compare_same_keys(old_value, new_value)
        compared[key] = compared_value
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
