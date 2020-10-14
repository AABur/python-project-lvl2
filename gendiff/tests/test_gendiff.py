"""Generate diff tests."""

from gendiff.scripts.gendiff import colollect_data, generate_diff

first_json = 'gendiff/tests/fixtures/file1.json'
second_json = 'gendiff/tests/fixtures/file2.json'
first_yaml = 'gendiff/tests/fixtures/file1.yaml'
second_yaml = 'gendiff/tests/fixtures/file2.yaml'
control_value = "{'follow': {'status': 'removed', 'value': False}, 'host': {'status': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'status': 'removed', 'value': '123.234.53.22'}, 'timeout': {'status': 'updated', 'old_value': 50, 'new_value': 20}, 'verbose': {'status': 'added', 'value': True}}"  # noqa:E501


def test_generate_diff():
    """Test - generate_diff."""
    assert generate_diff(first_json, second_json) == control_value


def test_collect_from_file():
    """Test - collect."""
    test = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert colollect_data(second_json) == test
