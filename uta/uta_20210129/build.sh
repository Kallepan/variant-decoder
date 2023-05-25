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

# Try to run the image
docker container rm -f $UTA_VERSION
docker volume rm uta_temp

docker volume create uta_temp
docker run -v /tmp:/tmp -v uta_temp:/var/lib/postgresql/data -e POSTGRES_PASSWORD=${UTA_PASS} --name $UTA_VERSION --network host kallepan/uta:${UTA_VERSION}