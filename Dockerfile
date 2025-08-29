FROM ubuntu:22.04

RUN apt update && apt upgrade -y

RUN apt install python3 python3-pip libglib2.0-0 -y

RUN pip install PyQt5

COPY . /IDArling

WORKDIR /IDArling

ENTRYPOINT ["python3", "idarling_server.py", "--no-ssl", "-h", "0.0.0.0"]