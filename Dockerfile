FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt update
RUN apt install gettext -y


COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
