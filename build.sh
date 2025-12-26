#!/usr/bin/env bash
# exit on error
set -o errexit

# Use pip instead of poetry
pip install -r requirements.txt

# Standard Django commands
python manage.py collectstatic --no-input
python manage.py migrate

# Only keep these if you actually have these files/commands in your project
# python manage.py loaddata seed_data.json
# python manage.py seed_admin