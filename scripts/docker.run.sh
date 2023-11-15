#!/usr/bin/env bash
PROJECT_NAME=fast-api-template/backend

if [[ $# -lt 1 ]]; then
  echo "$0 [.env file] ([docker run 이후에 넣을 값])"
  echo ""
  echo "첫 번 째 인자로 .env 파일의 path를 넣어주세요"
  echo "-----"
  echo "예) ./backend/.env 환경을 활성화 하고, bash를 실행"
  echo " > $0 ./backend/.env bash"
  exit 2
fi

docker run -it --rm \
  --env-file $1 \
  -p 8000:8000 \
  -p 8100:8100 \
 ${PROJECT_NAME} "${@:2}"
