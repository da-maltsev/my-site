fmt:
	poetry run ruff format src tests
	poetry run ruff check src tests --fix
	poetry run toml-sort pyproject.toml

lint:
	poetry run ruff format --check src tests
	poetry run ruff check src tests
	poetry run mypy src tests
	poetry run toml-sort pyproject.toml --check
	poetry run pymarkdown scan README.md

test:
	poetry run pytest --dead-fixtures