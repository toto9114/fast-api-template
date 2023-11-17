FROM python:3.11-buster

ENV PROJECT_DIR /app
ENV NGINX_UVICORN_ADDRESS 127.0.0.1:8000

RUN apt-get update && apt-get upgrade -y \
    && apt install -y sudo nginx unzip less gettext-base \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install poetry

RUN mkdir -p ${PROJECT_DIR} \
    && mkdir -p ${PROJECT_DIR}/logs \
    && useradd -u 1000 -ms /bin/bash -d /home/jihun -G sudo,staff,www-data jihun \
    && echo "jihun ALL=NOPASSWD: ALL" >> /etc/sudoers \
    && poetry config virtualenvs.create false

WORKDIR ${PROJECT_DIR}
COPY . .

RUN chmod +x ${PROJECT_DIR}/docker/run_command/* \
    && ln -s ${PROJECT_DIR}/docker/run_command/* /usr/local/bin/ \
    && rm -rf /etc/nginx/nginx.conf \
    && rm -rf /etc/nginx/sites-enabled/* \
#    && mv ${PROJECT_DIR}/docker/nginx/nginx.conf /etc/nginx/nginx.conf \
    && chown -R jihun:jihun /var/log/nginx /var/lib/nginx

RUN PIP_NO_CACHE_DIR=true poetry install --no-root --without dev \
    && chown -R jihun:jihun /app

ENV PATH=${PROEJCT_DIR}:${PATH}
ENV PYTHONPATH ${PATH}

USER jihun

VOLUME ["/app/logs"]
