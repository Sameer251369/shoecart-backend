#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static files for WhiteNoise
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Load your product data automatically
python manage.py loaddata seed_data.json

# If you have a custom command for the admin, keep it:
python manage.py seed_admin