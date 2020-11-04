# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest


@pytest.fixture()
def simple_before():
    return 'tests/fixtures/simple_before.yaml'


@pytest.fixture()
def simple_after():
    return 'tests/fixtures/simple_after.yaml'


@pytest.fixture()
def complex_before():
    return 'tests/fixtures/complex_before.json'


@pytest.fixture()
def complex_after():
    return 'tests/fixtures/complex_after.json'


@pytest.fixture()
def result_complex_json():
    return 'tests/fixtures/result_complex_json.txt'


@pytest.fixture()
def result_complex_plain():
    return 'tests/fixtures/result_complex_plain.txt'


@pytest.fixture()
def result_complex_structured():
    return 'tests/fixtures/result_complex_structured.txt'


@pytest.fixture()
def result_simple_json():
    return 'tests/fixtures/result_simple_json.txt'


@pytest.fixture()
def result_simple_plain():
    return 'tests/fixtures/result_simple_plain.txt'


@pytest.fixture()
def result_simple_structured():
    return 'tests/fixtures/result_simple_structured.txt'


@pytest.fixture()
def complex1_json():
    return 'tests/fixtures/old/complex01.json'


@pytest.fixture()
def complex2_json():
    return 'tests/fixtures/old/complex02.json'


@pytest.fixture()
def simple_data():
    return {
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


@pytest.fixture()
def complex_data():
    return {
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


@pytest.fixture()
def complex_result_s():
    return """{
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


@pytest.fixture()
def simple_result_s():
    return """{
    - follow: False
      host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: True
}"""


@pytest.fixture()
def complex_result_p():
    return ''.join(
        (
            " Property group1.baz was updated. From 'bas' to 'bars' \n",
            " Property group1.nest was updated. From '[complex value]' to 'str' \n",  # noqa:E501
            ' Property group2 was removed \n',
            " Property group3 was added with value: '[complex value]' \n",
        ),
    )


@pytest.fixture()
def simple_result_p():
    return ''.join(
        (
            ' Property follow was removed \n',
            ' Property proxy was removed \n',
            ' Property timeout was updated. From 50 to 20 \n',
            ' Property verbose was added with value: True \n',
        ),
    )


@pytest.fixture()
def result_data():
    return """{
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
