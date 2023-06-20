#!/bin/bash
#
# Create Kubernetes Secrets from local secrets.env
#

export $(grep -v '^#' ../.env | xargs)

echo ${DOCKER_REGISTRY_SERVER}


kubectl --kubeconfig=$KUBECONFIG \
    delete secret variant-decoder \
    -n genetics

kubectl --kubeconfig=$KUBECONFIG \
    create secret generic variant-decoder \
    --from-env-file=../.env \
    -n genetics

kubectl --kubeconfig=$KUBECONFIG \
    create secret docker-registry regcred \
    --docker-server=${DOCKER_REGISTRY_SERVER} \
    --docker-username=${DOCKER_REGISTRY_USERNAME} \
    --docker-password=${DOCKER_REGISTRY_PASSWORD} \
    -n genetics