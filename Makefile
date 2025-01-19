install:
	python3 -m pip install -r configuration/requirements.txt

migrate:
	./migration.sh

format-code:
	isort . && black .

lint:
	flake8

run:
	python3 -m main
