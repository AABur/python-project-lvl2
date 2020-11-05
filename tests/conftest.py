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
