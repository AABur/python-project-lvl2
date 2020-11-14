# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.loader import FileError, collect_data

wrong_json = 'tests/fixtures/wrong_json.json'
wrong_yaml = 'tests/fixtures/wrong_yaml.yaml'
wrong_ext = 'tests/fixtures/wrong_ext.ttt'
# file_missing = 'tests/fixtures/file_missing.json' # noqa:E800


@pytest.mark.parametrize(('file_path'), [
    wrong_json,
    wrong_yaml,
    wrong_ext,
    # file_missing, # noqa:E800
])
def test_file_error(file_path):
    with pytest.raises(FileError) as error:
        assert collect_data(file_path)
    assert str(error.value) == ''.join(('Not correct JSON/YAML file ', file_path, ' '))  # noqa:WPS441, E501
