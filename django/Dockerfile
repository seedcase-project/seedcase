FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk add curl

COPY . .

WORKDIR /home/app/django

ENTRYPOINT ["/home/app/django/entrypoint.sh"]
