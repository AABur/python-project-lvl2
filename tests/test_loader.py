# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.loader import WrongFileError, collect_data

correct_json = 'tests/fixtures/old/file1.json'
wrong_json = 'tests/fixtures/old/txt.json'
correct_yaml = 'tests/fixtures/old/file2.yaml'
wrong_yaml = 'tests/fixtures/old/txt.yaml'
wrong_ext = 'tests/fixtures/old/json1.txt'
file_missing = 'tests/fixtures/old/ttt.ttt'

json_data = {
    'host': 'hexlet.io',
    'timeout': 50,
    'proxy': '123.234.53.22',
    'follow': False,
}
yaml_data = {
    'host': 'hexlet.io',
    'timeout': 20,
    'verbose': True,
}


@pytest.mark.parametrize(('file_path', 'file_data'), [
    (correct_json, json_data),
    (correct_yaml, yaml_data),
])
def test_correct_file(file_path, file_data):
    assert collect_data(file_path) == file_data


@pytest.mark.parametrize(('file_path'), [
    wrong_json,
    wrong_yaml,
    wrong_ext,
    file_missing,
])
def test_wrong_file(file_path):
    with pytest.raises(WrongFileError) as file_error:
        assert collect_data(file_path)
    assert str(file_error.value) == 'Wrong file {0}'.format(file_path)  # noqa:WPS441, E501
