FROM postgres:15

ARG uta_version

ENV UTA_VERSION=$uta_version

RUN apt-get update && apt-get install -y curl
ENV PGDATA=/var/lib/postgresql/data/${UTA_VERSION}

# docker build
LABEL description="PostgreSQL image with $UTA_VERSION installed (https://github.com/Kallepan/variant-decoder/, adapted from: https://github.com/biocommons/uta)."

ADD load-uta.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/load-uta.sh
USER 999

EXPOSE 5432
CMD ["postgres"]