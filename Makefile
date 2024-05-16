.PHONY: lint format

lint:
	ruff check src
	mypy src

format:
	ruff format src