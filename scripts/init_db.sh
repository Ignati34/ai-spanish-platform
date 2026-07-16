#!/usr/bin/env bash
set -e
cd services/api
alembic upgrade head
python scripts/seed_demo_data.py
