#!/bin/bash
# Script for starting server

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

python manage.py runserver 0.0.0.0:8000
