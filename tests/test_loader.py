# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.loader import WrongFileError, collect_data

wrong_json = 'tests/fixtures/wrong_json.json'
wrong_yaml = 'tests/fixtures/wrong_yaml.yaml'
wrong_ext = 'tests/fixtures/wrong_ext.ttt'
file_missing = 'tests/fixtures/file_missing.json'


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
