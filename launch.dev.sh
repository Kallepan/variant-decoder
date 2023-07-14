#!/bin/bash

source venv/bin/activate

export $(grep -v '^#' ./.dev.env | xargs)

# Run the UTA webserver
python3 src/manage.py runserver 0:9000
