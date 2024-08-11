format:
    black .
    isort .
    ruff check --fix --exit-zero .

mypy:
    poetry run mypy -p syndb_cassandra
