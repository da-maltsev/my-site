fmt:
	poetry run ruff format app tests
	poetry run ruff check app tests --fix
	poetry run toml-sort pyproject.toml

lint:
	poetry run ruff format --check app tests
	poetry run ruff check app tests
	poetry run mypy app
	poetry run toml-sort pyproject.toml --check
	poetry run pymarkdown scan README.md

test:
	poetry run pytest --dead-fixtures
	poetry run pytest

server:
	cd app && poetry run uvicorn main:app --reload