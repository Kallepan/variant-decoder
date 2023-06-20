#!/bin/bash
#
# Builds the universal transcript archive (UTA) docker image from scratch. The official docker image is outdated, therefore I have recreated it.
#

export $(grep -v '^#' .env | xargs)

echo $DOCKER_REGISTRY_PASSWORD | docker login --username $DOCKER_REGISTRY_USERNAME --password-stdin

# Build and push uta
docker build --no-cache -f Dockerfile --build-arg uta_version=${UTA_VERSION} --build-arg http_proxy=$HTTP_PROXY --build-arg https_proxy=$HTTPS_PROXY -t kallepan/uta:${UTA_VERSION} .
docker tag kallepan/uta:${UTA_VERSION} kallepan/uta:latest
docker push kallepan/uta:${UTA_VERSION}

# Test/Run the UTA image
docker-compose down -v
docker-compose up