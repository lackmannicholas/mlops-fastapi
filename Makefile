install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

api: 
	fastapi dev api/main.py

test:
	python -m pytest

lint:
	pylint -rn .

format: 
	black .

venv:
	python -m venv .venv &&\
		source .venv/bin/activate