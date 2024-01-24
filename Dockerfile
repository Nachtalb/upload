FROM python:3.12-slim

WORKDIR /app
COPY . .

RUN set -x && \
    pip install poetry && \
    poetry install --no-dev

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["poetry", "run", "flask", "run"]
