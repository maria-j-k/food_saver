#!/bin/bash

export ENVIRONMENT="docker"

echo "apply migrations"
poetry run python food_saver_app/manage.py migrate

echo "starting the server"
poetry run python food_saver_app/manage.py runserver 0.0.0.0:8000
