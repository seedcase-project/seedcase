FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /home/app

RUN apk update; \
    apk add less openssh postgresql-dev gcc python3-dev musl-dev git npm

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk add curl

COPY . .

WORKDIR /home/app/seedcase

ENTRYPOINT ["/home/app/seedcase/entrypoint.sh"]
