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

if [ "$RUN_DUMPS" = "True" ]
then
  echo "Run dumps ${ENVIRONMENT}"
  python manage.py loaddata dumps/*.json

fi

exec python manage.py runserver 0.0.0.0:${APP_PORT}

exec "$@"