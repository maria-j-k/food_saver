FROM python:3.11.0

ARG ENVIRONMENT

ENV DRF_ENV=${ENVIRONMENT} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.2.2

RUN apt-get update && apt-get install -y build-essential libpq-dev python3-dev

RUN pip3 install pip==22.3
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/


# staging
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --without dev



COPY . /code
