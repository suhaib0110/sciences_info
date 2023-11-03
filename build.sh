#!/user/bin/env bash
set -o errexit # exit on error

pip install -r requirements.txt 

if [[-z $CREATE_SUPERUSER]]; then python manage.py createsuperuser

python manage.py  migrate

fi