#!/usr/bin/env sh
if [ "$RUN_MIGRATION" = "True" ]
then
  echo "Run Migrations ${ENVIRONMENT}"
  python manage.py migrate
fi

if [ "$RUN_COLLECTSTATIC" = "True" ]
then
  echo "Run Collectstatic ${ENVIRONMENT}"
  python manage.py collectstatic --no-input
fi

exec python manage.py runserver 0.0.0.0:${APP_PORT}

exec "$@"