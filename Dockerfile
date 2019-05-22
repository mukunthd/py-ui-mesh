FROM python:3.7

MAINTAINER Mukunthan Doraiswamy

COPY . /app
WORKDIR /app

CMD ["/app/run.py"]

EXPOSE 8080
