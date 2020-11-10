install: ## Install dependencies
	@poetry install

test: ## Run tests
	poetry run coverage run --source=gendiff -m pytest tests

lint: ## Run linter
	poetry run flake8 gendiff

selfcheck: ## Checks the validity of the pyproject.toml file
	poetry check

check: ## selfcheck + test + lint
	@make selfcheck
	@make test
	@make lint

build: ## Check and builds a package
	@make check
	@poetry build

cc-coverage: ## Prepare coverage report for Codeclimate
	poetry run coverage xml

help: ## This help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install test lint selfcheck check build cc-coverage help
.DEFAULT_GOAL := help
