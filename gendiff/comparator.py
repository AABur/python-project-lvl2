# -*- coding:utf-8 -*-
"""Calculate difference."""

STATUS = 'status'

ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

VALUE = 'value'
UPDATED_VALUE = 'updated_value'


# * Fixed WPS441, WPS440 to allow variable names to be reused in multiple loops
# * https://github.com/wemake-services/wemake-python-styleguide/pull/1768#pullrequestreview-550906165 # noqa:E501
def compile_diff(old_data, new_data):
    diff = {}
    keys_intersection = old_data.keys() & new_data.keys()
    for data_key in keys_intersection:
        diff[data_key] = _compare_same_keys(
            old_data.get(data_key), new_data.get(data_key),
        )
    keys_removed = old_data.keys() - new_data.keys()
    for data_key in keys_removed:  # noqa:WPS440
        diff[data_key] = {STATUS: REMOVED, VALUE: old_data.get(data_key)}  # noqa:WPS441, E501
    keys_added = new_data.keys() - old_data.keys()
    for data_key in keys_added:  # noqa:WPS440
        diff[data_key] = {STATUS: ADDED, VALUE: new_data.get(data_key)}  # noqa:WPS441, E501
    return diff


def _compare_same_keys(old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return compile_diff(old_value, new_value)
    if old_value == new_value:
        return {STATUS: UNCHANGED, VALUE: old_value}
    return {STATUS: UPDATED, VALUE: old_value, UPDATED_VALUE: new_value}
