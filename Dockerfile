FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo http://mirror.yandex.ru/mirrors/alpine/v3.10/main > /etc/apk/repositories; \
    echo http://mirror.yandex.ru/mirrors/alpine/v3.10/community >> /etc/apk/repositories

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && pip3 install pipenv

# Requirements are installed here to ensure they will be cached.
COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock
RUN cd /app && pipenv install --dev --ignore-pipfile

COPY ./start_dev/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./start_dev/runserver /runserver
RUN sed -i 's/\r$//g' /runserver
RUN chmod +x /runserver

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
