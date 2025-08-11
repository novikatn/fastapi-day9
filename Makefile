lint:
	uv run ruff format .
	uv run ruff check . --fix

dev:
	uv run uvicorn app.main:app --reload

composeProd:
	docker compose -f docker-compose.prod.yml up --build

# celery:
# uv run celery -A app.celery_app worker -c 2 -l info