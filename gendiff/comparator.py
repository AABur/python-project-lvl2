# -*- coding:utf-8 -*-

STATUS = 'status'

ADDED = 'added'
NESTED = 'nested'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
UPDATED = 'updated'

VALUE = 'value'
UPDATED_VALUE = 'updated_value'


# * Fixed WPS441, WPS440 to allow variable names to be reused in multiple loops
# * https://github.com/wemake-services/wemake-python-styleguide/pull/1768#pullrequestreview-550906165 # noqa:E501
def compile_diff(first_data_set, second_data_set):
    diff = {}
    keys_intersection = first_data_set.keys() & second_data_set.keys()
    for data_key in keys_intersection:
        diff[data_key] = compare_same_keys(
            first_data_set.get(data_key), second_data_set.get(data_key),
        )
    keys_removed = first_data_set.keys() - second_data_set.keys()
    for data_key in keys_removed:  # noqa:WPS440
        diff[data_key] = {STATUS: REMOVED, VALUE: first_data_set.get(data_key)}  # noqa:WPS441, E501
    keys_added = second_data_set.keys() - first_data_set.keys()
    for data_key in keys_added:  # noqa:WPS440
        diff[data_key] = {STATUS: ADDED, VALUE: second_data_set.get(data_key)}  # noqa:WPS441, E501
    return diff


def compare_same_keys(first_value, second_value):
    if isinstance(first_value, dict) and isinstance(second_value, dict):
        return {STATUS: NESTED, VALUE: compile_diff(first_value, second_value)}
    if first_value == second_value:
        return {STATUS: UNCHANGED, VALUE: first_value}
    return {STATUS: UPDATED, VALUE: first_value, UPDATED_VALUE: second_value}
