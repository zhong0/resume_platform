FROM ubuntu:22.04

RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y

WORKDIR /app
COPY ./app/requirement.txt /app/requirement.txt

RUN pip install -r /app/requirement.txt

EXPOSE 6060
