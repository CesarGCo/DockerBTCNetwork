FROM python:3.10-slim

WORKDIR /app

RUN pip install Flask

RUN pip install psycopg2-binary

COPY . .

CMD ["python", "app.py"]