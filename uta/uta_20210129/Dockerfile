FROM postgres:15

ARG http_proxy
ARG https_proxy
ARG uta_version

ENV http_proxy $http_proxy
ENV https_proxy $https_proxy

RUN apt-get update && apt-get install -y curl

# docker build
ENV UTA_VERSION $uta_version
ENV PGData=/var/lib/postgresql/data
LABEL description="PostgreSQL image with $UTA_VERSION installed (https://github.com/Kallepan/variant-decoder/, adapted from: https://github.com/biocommons/uta)."

ADD load-uta.sh /docker-entrypoint-initdb.d/
