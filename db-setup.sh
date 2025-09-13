#!/bin/bash
# Check if .db.lock exists
if [ -f .db.lock ]; then
    echo "db.lock exists, doing nothing"
    exit 0
fi
echo "db.lock does not exist, setting up database"
touch .db.lock
uv run --env-file=.env python -m src.database.setup
