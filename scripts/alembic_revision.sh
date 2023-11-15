#!/usr/bin/env bash
alembic revision --autogenerate "${@:1}"
