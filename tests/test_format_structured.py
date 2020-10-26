# -*- coding:utf-8 -*-
"""Test plain format generator."""
import pytest

from gendiff.formaters.format_structured import render

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

simple_result = """{
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True
}"""

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

complex_result = """{
    group1: {
        - baz: bas
        + baz: bars
          foo: bar
        - nest: {
            key: value
        }
        + nest: str
    }
    - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
    + group3: {
        fee: 100500
        deep: {
            id: {
                number: 45
            }
        }
    }
}"""


@pytest.mark.parametrize(('test_data', 'test_result'), [
    (simple_data, simple_result),
    (complex_data, complex_result),
])
def test_print_structured(test_data, test_result):
    assert render(test_data) == test_result
