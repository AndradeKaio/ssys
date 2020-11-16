#!/bin/sh

# Apply database migrations
printf "\n[2] APPLY DATABASE MIGRATIONS\n\n"
python manage.py makemigrations api
python manage.py migrate
# Apply database migrations

printf "\n[3] CREATE USER\n\n"
python manage.py createuser

printf "\n[3] SEEDING BASE INFORMATION\n\n"
python manage.py loaddata employee.json

printf "\nSTARTUP FINISHED!\n\n"
exec "$@"