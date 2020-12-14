FROM python:3.7-alpine


RUN apk add build-base

WORKDIR /app
COPY ./requirements.txt ./app/requirements.txt

RUN pip install --upgrade pip && pip install -r ./app/requirements.txt
COPY . ./app
EXPOSE 8080
