# Eventex

Sistema de Eventos

[![Build Status](https://travis-ci.org/hugodieb/eventex.svg?branch=master)](https://travis-ci.org/hugodieb/eventex)
[![Code Health](https://landscape.io/github/hugodieb/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/hugodieb/eventex/master)


## Como desenvolver?

1. Clone do repositório
2. Crie um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as depêndencias
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/hugodieb/eventex.git project
cd project
python -m venv .myenv
source .myenv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG:False
# Configuro o email
git push heroku master --force
```