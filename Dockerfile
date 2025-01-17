FROM python:3.12-slim

WORKDIR /app

COPY /pyproject.toml /poetry.lock /README.md /app/

RUN pip install poetry
COPY /telebot_template/ /app/telebot_template

RUN poetry install

CMD ["poetry", "run", "start"]
