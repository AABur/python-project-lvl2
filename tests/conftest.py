# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest


@pytest.fixture()
def result_data():
    return {
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


@pytest.fixture()
def complex1_json():
    return 'tests/fixtures/complex1.json'


@pytest.fixture()
def complex2_json():
    return 'tests/fixtures/complex2.json'
