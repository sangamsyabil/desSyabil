#!/usr/bin/env bash

# Jenkins build script
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

echo "=================================================="
echo "Runnig the test"
echo "=================================================="
python manage.py jenkins

echo "=================================================="
echo "Running flake8"
echo "=================================================="
flake8

echo "=================================================="
echo "Done!"
