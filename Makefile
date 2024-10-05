install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run: 
	fastapi dev api/app.py

test:
	python -m pytest

lint:
	pylint -rn api

format: 
	black api/*.py

venv:
	python -m venv .venv &&\
		source .venv/bin/activate