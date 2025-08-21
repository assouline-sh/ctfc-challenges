FROM python:3.9-slim

WORKDIR /app

COPY . /app

EXPOSE 5432

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--host=0.0.0.0", "--port=5432"]

