#!/bin/bash

# launch.sh

sleep 15

gunicorn variant_decoder.wsgi:application --bind 0.0.0.0:9000 --workers 3