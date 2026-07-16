COMPOSE=docker compose -f infra/compose/docker-compose.yml --env-file .env
SELF=docker compose -f infra/compose/docker-compose.selfhosted.yml --env-file .env.selfhosted

.PHONY: env up down logs migrate seed web-dev api-dev selfhosted selfhosted-down

env:            ## create .env files from examples
	cp -n .env.example .env || true
	cp -n .env.selfhosted.example .env.selfhosted || true
	cp -n apps/web/.env.example apps/web/.env || true

up:             ## build + run full stack (web:8080, api:8000)
	$(COMPOSE) up --build

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

migrate:        ## create tables inside the api container
	$(COMPOSE) exec api python scripts/create_tables.py

seed:           ## seed levels A1-C2, plans, demo lessons, admin
	$(COMPOSE) exec api python scripts/seed_demo_data.py

selfhosted:     ## desktop/self-hosted: everything in Docker, auto-migrate+seed
	$(SELF) up --build

selfhosted-down:
	$(SELF) down

web-dev:        ## run the web app locally (Vite) on :3000
	cd apps/web && npm install && npm run dev

api-dev:        ## run the API locally (needs local postgres/redis)
	cd services/api && uvicorn app.main:app --reload
