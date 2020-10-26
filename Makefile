install:
	@poetry install

test:
	poetry run coverage run --source=gendiff -m pytest tests

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

cc-coverage:
	poetry run coverage xml

.PHONY: install test lint selfcheck check build cc-coverage
