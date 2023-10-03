FROM python:3.10

WORKDIR /tasty_delivery

COPY poetry.lock pyproject.toml /tasty_delivery/

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-root --no-dev

COPY tasty_delivery/ tasty_delivery/

ENTRYPOINT uvicorn tasty_delivery.server:app --host 0.0.0.0 --port 8000