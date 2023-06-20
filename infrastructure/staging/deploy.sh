#!/bin/bash

VERSION=dev # Change this to the version you want to deploy

export $(grep -v '^#' ../../.env | xargs)

echo $DOCKER_REGISTRY_PASSWORD | docker login --username $DOCKER_REGISTRY_USERNAME --password-stdin

cd ../../.
docker build -f Dockerfile.staging -t kallepan/variant-decoder:$VERSION .
docker push kallepan/variant-decoder:$VERSION

cd infrastructure/prod
kubectl --kubeconfig=$KUBECONFIG apply -f manifest.yaml
