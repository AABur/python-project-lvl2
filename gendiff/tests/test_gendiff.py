"""Generate diff tests."""

from gendiff.scripts.gendiff import (
    collect_data_from_file,
    combine_data,
    generate_diff,
)

first_file = 'gendiff/tests/file1.json'
second_file = 'gendiff/tests/file2.json'
control_value = '- follow: False;  host: hexlet.io;- proxy: 123.234.53.22;- timeout: 50;+ timeout: 20;+ verbose: True'  # noqa:E501


def test_generate_diff():
    """Test - generate_diff."""
    assert generate_diff(first_file, second_file) == control_value


def test_combine_data():
    """Test - combine_data."""
    first_data = {
        'key_rem': 'removed',
        'key_upd': 'old',
        'key_unc': 5,
    }
    second_data = {
        'key_upd': 'new',
        'key_unc': 5,
        'key_add': 'added',
    }
    combined_data = {
        'key_rem': ['removed', None],
        'key_upd': ['old', 'new'],
        'key_unc': [5, 5],
        'key_add': [None, 'added'],
    }
    assert combine_data(first_data, second_data) == combined_data


def test_collect_data_from_file():
    """Test - collect_data."""
    test_data = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert collect_data_from_file(second_file) == test_data
