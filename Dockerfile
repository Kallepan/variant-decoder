# pull official base image
FROM python:3.9.15-buster as builder

# setup environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Necessary for Docker building behind a proxy
ENV http_proxy=http://proxy.labmed.de:8080/
ENV https_proxy=http://proxy.labmed.de:8080/

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt
RUN chown -R www-data:www-data .


#########
# FINAL #
#########

FROM python:3.9.15-buster

# Necessary for Docker building 
ENV http_proxy=http://proxy.labmed.de:8080/
ENV https_proxy=http://proxy.labmed.de:8080/

RUN useradd -ms /bin/bash app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir ${APP_HOME}
WORKDIR ${APP_HOME}

# install dependencies
RUN apt-get update && apt-get install nano postgresql netcat -y --no-install-recommends
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY launch.sh ${APP_HOME}
COPY src/ ${APP_HOME}

RUN chmod -R 775 ${APP_HOME}/launch.sh
RUN chown -R app:app ${APP_HOME}

USER app

# start server
ENTRYPOINT ["/home/app/web/launch.sh"]