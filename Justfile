format:
    poetry run black .
    poetry run isort .
    poetry run ruff check . --fix

mypy:
    poetry run mypy -p syndb_cassandra
