# -*- coding:utf-8 -*-

import pytest

from gendiff.loader import GendiffFileError, collect_data


@pytest.mark.parametrize(
    'file_path',
    [
        ('tests/fixtures/wrong_ext.ttt'),
        ('tests/fixtures/wrong_json.json'),
        ('tests/fixtures/wrong_yaml.yaml'),
        ('file_not_exists'),
    ],
)
def test_wrong_file(file_path):
    with pytest.raises(GendiffFileError):
        assert collect_data(file_path)
