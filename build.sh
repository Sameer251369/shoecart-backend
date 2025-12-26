#!/usr/bin/env bash
# exit on error
set -o errexit

# Use poetry if that is your tool
poetry install  

# Standard Django commands
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata seed_data.json
python manage.py seed_admin