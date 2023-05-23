#!/bin/bash

# launch.sh

# wait for postgres
sleep 15

python manage.py migrate --no-input

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
    (echo "Config is done :)")
fi

gunicorn molg_app.wsgi:application --bind 0.0.0.0:9000 --workers 3