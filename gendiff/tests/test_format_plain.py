# -*- coding:utf-8 -*-
"""Test plain format generator."""
import pytest

from gendiff.formaters.format_plain import print_plain

simple_data = {
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

simple_result = ''.join(
    (
        ' Property follow was removed \n',
        ' Property proxy was removed \n',
        ' Property timeout was updated. From 50 to 20 \n',
        ' Property verbose was added with value: True \n',
    ),
)

complex_data = {
    'group1': {
        'baz': {
            'status': 'updated',
            'value': 'bas',
            'updated_value': 'bars',
        },
        'foo': {
            'status': 'unchanged',
            'value': 'bar',
        },
        'nest': {
            'status': 'updated',
            'value': {'key': 'value'},
            'updated_value': 'str',
        },
    },
    'group2': {
        'status': 'removed',
        'value': {'abc': 12345, 'deep': {'id': 45}},
    },
    'group3': {
        'status': 'added',
        'value': {'fee': 100500, 'deep': {'id': {'number': 45}}},
    },
}

complex_result = ''.join(
    (
        " Property group1.baz was updated. From 'bas' to 'bars' \n",
        " Property group1.nest was updated. From '[complex value]' to 'str' \n",
        ' Property group2 was removed \n',
        " Property group3 was added with value: '[complex value]' \n",
    ),
)


@pytest.mark.parametrize(('test_data', 'test_result'), [
    (simple_data, simple_result),
    (complex_data, complex_result),
])
def test_print_plain(test_data, test_result):
    assert print_plain(test_data) == test_result
