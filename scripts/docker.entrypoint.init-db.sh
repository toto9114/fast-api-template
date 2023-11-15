#!/usr/bin/env bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER developer;
	CREATE DATABASE developer;
	GRANT ALL PRIVILEGES ON DATABASE developer TO developer;
EOSQL
