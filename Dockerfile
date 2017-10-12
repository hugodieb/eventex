# Container base: python 3.6 
FROM python:3.6

# Update
RUN apt-get update

RUN pip install uwsgi

RUN apt-get -y install nano nginx

ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /app

# "Copia" arquivo requirements.txt para o diretorio app
COPY requirements.txt requirements.txt

# Executa o pip
RUN pip install -r requirements.txt

ENV DATABASE_USER=eventex
ENV DATABASE_NAME=eventex_dev
ENV DATABASE_PORT=5432
ENV DATABASE_HOST=172.17.0.1
ENV DATABASE_PASS=eventex

RUN mkdir /uwsgi	

COPY docker/bin/* /usr/local/bin/
COPY docker/uwsgi.ini /uwsgi.ini

RUN chmod +x /usr/local/bin/start.sh

# "Copia" os arquivos locais para o diretorio code no container 
COPY . /app	 	