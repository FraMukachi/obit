#!/bin/bash
# Orbit Platform Setup Script

# Install Django
pip install django

# Create Django project
django-admin startproject orbit .

# Create all apps
python manage.py startapp accounts
python manage.py startapp profiles
python manage.py startapp chat
python manage.py startapp currency

# Create necessary directories
mkdir -p static/css templates/registration media

echo "Setup complete!"
