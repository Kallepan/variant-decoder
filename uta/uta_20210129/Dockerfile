FROM postgres:15

ARG http_proxy
ARG https_proxy
ARG uta_version

ENV http_proxy $http_proxy
ENV https_proxy $https_proxy

RUN apt-get update && apt-get install -y curl

RUN groupadd -r uta && useradd -r -g uta uta
RUN chown -R uta:uta /var/lib/postgresql/data

# docker build
ENV UTA_VERSION $uta_version
ENV PGData=/var/lib/postgresql/data
LABEL description="PostgreSQL image with $UTA_VERSION installed (https://github.com/Kallepan/variant-decoder/, adapted from: https://github.com/biocommons/uta)."


ADD load-uta.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/load-uta.sh
USER uta

EXPOSE 5432