#!/bin/bash

# launch.sh

sleep 15
seqrepo -r $HGVS_SEQREPO pull

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "seqrepo pull successful.Setting up seqrepo"
    export HGVS_SEQREPO_DIR="${HGVS_SEQREPO}/${UTA_VERSION}"
else
    echo "seqrepo pull failed. Using network access"
fi
gunicorn variant_decoder.wsgi:application --bind 0.0.0.0:9000 --workers 3