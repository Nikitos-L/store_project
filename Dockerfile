FROM python:3.13-alpine
RUN adduser --disabled-password store-user

RUN pip install --upgrade pip

EXPOSE 8000

WORKDIR /subs_store
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY subs_store /subs_store

USER store-user