# Container base: python 3.6 
FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Cria diretório onde vão ficar os fontes
RUN mkdir /app

# Define o diretório de trabalho
WORKDIR /app

# "Copia" arquivo requirements.txt para o diretorio code
ADD requirements.txt /app/

# Update
RUN apt-get update

# Executa o pip
RUN pip install -r requirements.txt

ENV DATABASE_USER=eventex
ENV DATABASE_NAME=eventex_dev
ENV DATABASE_PORT=5432
ENV DATABASE_HOST=172.17.0.1
ENV DATABASE_PASS=eventex

# "Copia" os arquivos locais para o diretorio code no container 
ADD . /app/ 