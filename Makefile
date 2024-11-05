install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt -e .

dev: 
	fastapi dev app.py

test:
	python -m pytest -v --cov=nlp

lint:
	pylint -rn *.py

format: 
	black .

venv:
	python -m venv .venv &&\
		source .venv/bin/activate