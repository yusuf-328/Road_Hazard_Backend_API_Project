# Road Hazard Tracker API

## Description

Road Hazard Tracker API is a backend REST API built using Django Rest Framework. It allows users to report and manage road hazards securely using JWT authentication.

## Features

- Create hazard reports
- Retrieve hazards
- Update hazards
- Delete hazards
- JWT authentication
- Role-based permissions

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- SimpleJWT

## Setup

Clone repository:

git clone <repo link>

Create virtual environment:

python -m venv venv

Activate:

source venv/Scripts/activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Run server:

python manage.py runserver

## API Endpoints

GET /api/hazards/

POST /api/hazards/

PUT /api/hazards/<id>/

DELETE /api/hazards/<id>/

POST /api/token/

POST /api/token/refresh/

## Author

Shile Yusuf