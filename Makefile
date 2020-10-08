install:
	@poetry install

test:
	poetry run coverage run --source=gendiff -m pytest gendiff

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
