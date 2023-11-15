#!/bin/bash
cd ${PROJECT_DIR}
exec su -c "uvicorn backend.main:app --host 0.0.0.0 --port 8000" jihun
