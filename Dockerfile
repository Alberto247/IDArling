FROM Ubuntu:22.04

RUN apt update && apt upgrade -y

COPY . /IDArling

WORKDIR /IDArling

ENTRYPOINT ["python3", "idarling_server.py", "--no-ssl"]