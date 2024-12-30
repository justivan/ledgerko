FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends libpq-dev wait-for-it

COPY requirements /tmp/pip-tmp/requirements
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements/local.txt \
   && rm -rf /tmp/pip-tmp

COPY docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY .devcontainer/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]
