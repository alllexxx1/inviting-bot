install:
	pip install -r requirements.txt

migrate:
	./migration.sh

format-code:
	isort . && black .

lint:
	flake8

run:
	python3 -m main