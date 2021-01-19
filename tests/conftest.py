# -*- coding:utf-8 -*-

import pytest


@pytest.fixture()
def simple_before_path():
    return 'tests/fixtures/simple/before.yaml'


@pytest.fixture()
def simple_after_path():
    return 'tests/fixtures/simple/after.yaml'


@pytest.fixture()
def complex_before_path():
    return 'tests/fixtures/complex/before.json'


@pytest.fixture()
def complex_after_path():
    return 'tests/fixtures/complex/after.json'


@pytest.fixture()
def result_complex_json():
    return 'tests/fixtures/complex/result_json.txt'


@pytest.fixture()
def result_complex_plain():
    return 'tests/fixtures/complex/result_plain.txt'


@pytest.fixture()
def result_complex_stylish():
    return 'tests/fixtures/complex/result_stylish.txt'


@pytest.fixture()
def result_simple_json():
    return 'tests/fixtures/simple/result_json.txt'


@pytest.fixture()
def result_simple_plain():
    return 'tests/fixtures/simple/result_plain.txt'


@pytest.fixture()
def result_simple_stylish():
    return 'tests/fixtures/simple/result_stylish.txt'
