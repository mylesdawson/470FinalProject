#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
# fi
# echo "Waiting for postgres..."

# while ! nc -z $SQL_HOST $SQL_PORT; do
#   sleep 0.1
# done

# echo "PostgreSQL started"

# python manage.py flush --no-input
# python manage.py migrate

# exec "$@"


python /code/skedge/manage.py flush --no-input
python /code/skedge/manage.py makemigrations
python /code/skedge/manage.py migrate
python /code/skedge/manage.py runserver 0.0.0.0:8080