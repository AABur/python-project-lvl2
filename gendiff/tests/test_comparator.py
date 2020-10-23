# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.comparator import generate_diff

complex1_json = 'gendiff/tests/fixtures/complex1.json'
complex2_json = 'gendiff/tests/fixtures/complex1.json'

result_data = {
    'group1': {
        'status': 'unchanged',
        'value': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {'key': 'value'},
        },
    },
    'group2': {
        'status': 'unchanged',
        'value': {
            'abc': 12345,
            'deep': {'id': 45},
        },
    },
}


@pytest.mark.parametrize(('file1', 'file2', 'diff'), [
    (complex1_json, complex2_json, result_data),
])
def test_generate_diff(file1, file2, diff):
    assert generate_diff(file1, file2) == diff
