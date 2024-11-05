install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt -e .

dev: 
	fastapi dev app.py

docker-build:
	docker build -t mlops-fastapi:latest .

docker-run:
	docker stop mlops-fastapi
	docker rm mlops-fastapi
	docker run --name mlops-fastapi -p 8000:8000 mlops-fastapi

test:
	python -m pytest -v --cov=nlp

lint:
	pylint -rn *.py

format: 
	black .

venv:
	python -m venv .venv &&\
		source .venv/bin/activate