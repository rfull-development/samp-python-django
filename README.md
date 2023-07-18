# samp-python-django
This repository is a sample for Django.

## Get Started
### Execute on Linux
1. Install virtual environment
    ```bash
    python -m venv .env
    ```
1. Change virtual environment
    ```bash
    source .env/bin/activate
    ```
1. Install packages
    ```bash
    pip install -r requirements.txt
    ```
1. Execute API server
    ```bash
    export SECRET_KEY='<YOUR SECRET KEY>'
    cd service
    python manage.py makemigrations api
    python manage.py migrate
    python manage.py runserver
    ```
