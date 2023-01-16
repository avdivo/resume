# pull the official docker image
FROM python:3.10-slim-buster

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/
ADD . /code/
RUN pip install -r requirements.txt
