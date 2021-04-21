FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VERSION=1.1.4

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # psql is still used in some scripts
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root

WORKDIR /app

COPY . /app
