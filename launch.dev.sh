#!/bin/bash

source venv/bin/activate

export $(grep -v '^#' ./.dev.env | xargs)

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@example.com


python3 src/manage.py makemigrations
python3 src/manage.py migrate
python3 src/manage.py createsuperuser --no-input
python3 src/manage.py runserver 0:9000
