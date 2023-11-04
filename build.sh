#!/usr/bin/env bash

set -o errexit  # exit on error

python manage.py collectstatic --no-input
python manage.py migrate

pip install -r requirements.txt
