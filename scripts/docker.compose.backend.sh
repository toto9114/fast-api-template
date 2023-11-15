#!/usr/bin/env bash
set -e
PROJECT_NAME=fast-api-template/backend
COMPOSE_FILE=$(pwd)/docker/compose/compose.backend.yml

export ENV_FILE_PATH=$(pwd)/backend/.env

exec docker-compose \
  --file ${COMPOSE_FILE} \
  --project-name fast-api-template \
  "$@"
