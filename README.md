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

### Docker Image
#### In development mode
run
```bash
        export ENVIRONMENT=docker-dev
        docker compose up --build
```
If you want to stop the container but have the data you've entered to database persist, run

```bash
         docker compose stop
```

Than to restart the same container with the data in the database, run

```bash
         docker compose start
```

If you want to destroy the container and the created database, run

```bash
         docker compose down
```

If you want to recreate the container but don't need to rebuild the image run
```bash
        docker compose up
```


#### As staging
```bash
        export ENVIRONMENT=docker
        docker compose -f docker-compose-staging.yaml up --build
```
The database is persisting, so you can use `stop` or `down` commnad, it will not affect the database contnet.

You can start, stop, bring up or down the container using the same commands as in the previous section, you just need
to provide the additional argument `-f docker-compose-staging.yaml` after the `docker compose` command.
