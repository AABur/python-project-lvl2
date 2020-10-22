# -*- coding:utf-8 -*-
"""Test plain format generator."""


from gendiff.format_plain import print_plain

test_data = {
    'follow':
        {
            'status': 'removed',
            'value': False,
        },
    'host':
        {
            'status': 'unchanged',
            'value': 'hexlet.io',
        },
    'proxy':
        {
            'status': 'removed',
            'value': '123.234.53.22',
        },
    'timeout':
        {
            'status': 'updated',
            'value': 50,
            'updated_value': 20,
        },
    'verbose':
        {
            'status': 'added',
            'value': True,
        },
}

test_result = """ Property follow was removed
 Property proxy was removed
 Property timeout was updated. From 50 to 20
 Property verbose was added with value: True \n"""


def test_print_plain():
    assert print_plain(test_data) == test_result
