# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.comparator import generate_diff

complex1_json = 'tests/fixtures/complex1.json'
complex2_json = 'tests/fixtures/complex2.json'

result_data = {
    'group1': {
        'baz': {
            'status': 'updated',
            'updated_value': 'bars',
            'value': 'bas',
        },
        'foo': {
            'status': 'unchanged',
            'value': 'bar',
        },
        'nest': {
            'status': 'updated',
            'updated_value': 'str',
            'value': {
                'key': 'value',
            },
        },
    },
    'group2': {
        'status': 'removed',
        'value': {
            'abc': 12345,
            'deep': {'id': 45},
        },
    },
    'group3': {
        'status': 'added',
        'value': {
            'deep': {
                'id': {'number': 45},
            },
            'fee': 100500,
        },
    },
}


@pytest.mark.parametrize(('file1', 'file2', 'diff'), [
    (complex1_json, complex2_json, result_data),
])
def test_generate_diff(file1, file2, diff):
    assert generate_diff(file1, file2) == diff
