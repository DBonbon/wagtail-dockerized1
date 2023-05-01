FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

# Install system packages required by Wagtail and Django.
# https://github.com/wagtail/wagtail/blob/v4.0.2/wagtail/project_template/Dockerfile
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown django /start

WORKDIR /app

# avoid 'permission denied' error
RUN mkdir /app/media

# copy project code
COPY . .

RUN chown -R django:django /app

USER django

ENTRYPOINT ["/entrypoint"]
