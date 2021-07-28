FROM python:3.7
MAINTAINER Lucas M. Sing

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /market-API
COPY ./src /market-API
WORKDIR /market-API

RUN export PYTHONPATH='/usr/lib/python3/dist-packages'
ENV PYTHONPATH='/usr/lib/python3/dist-packages'

# -D is only to run the apps without root premision
# RUN adduser user
# RUN adduser -D user
# USER user
