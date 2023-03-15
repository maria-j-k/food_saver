# Food Saver API
The application intends to help managing cooking in terms of planning courses and use up the ingredients.

## Prerequisites
- python-dev or python3-dev
- libpq-dev
- postgres
- poetry

## Setup

### Locally

- clone the repository
- create the postgres database
- edit the `sample_env` file providing your credentials and other variables (as db name) and save it as `.env` file
- run
```bash
    poetry config virtualenvs.create false --local
```
You can ommit this and next step an use poetry's virtual environment. It that case you'd need to preceed all
subsequent commands with `poetry run`
- create and activate virtual environment
- run `poetry install`
- cd into `food_saver_app` directory
- run `python manage.py migrate`
- run `python manage.py createsuperuser`
- run `python manage.py runserver`
