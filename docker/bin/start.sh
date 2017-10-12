#!/bin/bash
cd /app
./manage.py collectstatic --noinput
./manage.py migrate --noinput
uwsgi --ini /uwsgi.ini	