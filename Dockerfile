FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /code
ADD ./ /code

ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_DATABASE
ARG DB_PORT
ARG DB_HOST
ARG APP_PORT

ENV MYSQL_USER=${MYSQL_USER}
ENV APP_PORT=${APP_PORT}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV DB_PORT=${DB_PORT}
ENV DB_HOST=${DB_HOST}

RUN apt-get update && apt-get install -y --no-install-recommends python3-dev

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]
