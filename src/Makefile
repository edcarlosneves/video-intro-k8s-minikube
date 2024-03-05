SHELL := /bin/bash

run-server:
	uvicorn app.generate_order:app --reload

api-test:
	curl -X POST http://localhost:8000/new_order

docker-build:
	docker build -f Dockerfile.$(OPERATING_SYSTEM) -t edcarlosneves/generate_order:$(OPERATING_SYSTEM) .  