install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint

test:
	pytest -v

deploy:
	# deploy

all: install format