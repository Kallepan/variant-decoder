#!/bin/bash

VERSION=v1 # Change this to the version you want to deploy

export $(grep -v '^#' ../../.env | xargs)

echo $DOCKER_REGISTRY_PASSWORD | docker login --username $DOCKER_REGISTRY_USERNAME --password-stdin

cd ../../.
docker build -t kallepan/variant-decoder:$VERSION .
docker push kallepan/variant-decoder:$VERSION

cd infrastructure/prod
cp manifest.yaml run.yaml
sed -i "s/IMAGE_TAG/$VERSION/g" run.yaml
kubectl --kubeconfig=$KUBECONFIG apply -f run.yaml
