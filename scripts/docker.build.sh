#!/usr/bin/env bash
PROJECT_NAME=fast-api-template/backend

docker build --network host -t ${PROJECT_NAME} .
