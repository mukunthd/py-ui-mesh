FROM python:3.7

MAINTAINER Mukunthan Doraiswamy

COPY . /app
WORKDIR /app

CMD ["run.py"]

EXPOSE 8080
