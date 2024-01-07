install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	pylint

test:
	# test

deploy:
	# deploy

all: install format