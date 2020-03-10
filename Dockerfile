FROM python:3-alpine
WORKDIR /app
COPY requirements.txt /app
COPY . /app

CMD python3 app.py
