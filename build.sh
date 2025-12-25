#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static files for WhiteNoise
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Run your custom command to create the admin user
python manage.py seed_admin

# Optional: Load your product data if you have the json file
# python manage.py loaddata seed_data.json