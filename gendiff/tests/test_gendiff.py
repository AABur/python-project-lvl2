"""Generate diff tests."""


from gendiff.loader import collect_data

first_json = 'gendiff/tests/fixtures/file1.json'
second_json = 'gendiff/tests/fixtures/file2.json'
first_yaml = 'gendiff/tests/fixtures/file1.yaml'
second_yaml = 'gendiff/tests/fixtures/file2.yaml'
control_value = "{'follow': {'status': 'removed', 'value': False}, 'host': {'status': 'unchanged', 'value': 'hexlet.io'}, 'proxy': {'status': 'removed', 'value': '123.234.53.22'}, 'timeout': {'status': 'updated', 'value': 50, 'updated_value': 20}, 'verbose': {'status': 'added', 'value': True}}"  # noqa:E501


def test_collect_from_file():
    """Test - collect."""
    test = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert collect_data(second_yaml) == test
