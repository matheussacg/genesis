#!/bin/bash
# Verifica se o parâmetro foi passado
if [ "$1" == "prod" ]; then
    export ENV=prod
    alembic upgrade head
    uvicorn main:app --host 0.0.0.0 --port 8000 --log-level info
elif [ "$1" == "dev" ]; then
    export ENV=dev
    alembic upgrade head
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
else
    echo "Usage: $0 {dev|prod}"
    exit 1
fi