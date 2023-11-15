FROM python:3.11-buster

ENV PROJECT_DIR /srv/fast-api-template
ENV NGINX_UVICORN_ADDRESS 127.0.0.1:8000

RUN apt-get update && apt-get upgrade -y \
    && apt install -y sudo nginx unzip less gettext-base \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install supervisor poetry \
    && poetry config virtualenvs.create false

RUN mkdir -p ${PROJECT_DIR} \
    && mkdir -p ${PROJECT_DIR}/logs \
    && mkdir -p /srv/logs/nginx \
    && mkdir -p /srv/logs/uwsgi \
    && chmod -R 775 /srv/logs \
    && useradd -u 1000 -ms /bin/bash -d /home/jihun -G sudo,staff,www-data jihun \
    && echo "jihun ALL=NOPASSWD: ALL" >> /etc/sudoers

WORKDIR ${PROJECT_DIR}
COPY . .

RUN chmod +x ${PROJECT_DIR}/docker/run_command/* \
    && ln -s ${PROJECT_DIR}/docker/run_command/* /usr/local/bin/ \
    && rm -rf /etc/nginx/nginx.conf \
    && rm -rf /etc/nginx/sites-enabled/* \
    && mv ${PROJECT_DIR}/docker/nginx/nginx.conf /etc/nginx/nginx.conf

RUN PIP_NO_CACHE_DIR=true poetry install --no-root --without dev \
    && chown -R jihun:jihun /srv

ENV PATH=${PROEJCT_DIR}:${PATH}
ENV PYTHONPATH ${PATH}

VOLUME ["/srv/fast-api-template/logs", "/srv/logs"]
