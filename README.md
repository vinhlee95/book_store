# Django GraphQL
Check how GraphQL works in Django

## Technologies
- [Poetry](https://python-poetry.org/docs/): Python package manager
- [Django](https://www.djangoproject.com/): Python backend framework
- Docker

## Install packages
`poetry install`

## Run migration and run server
```shell
poetry shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Run the server in Docker container
* Build the Docker image with tag
* Run the built docker image and expose the container port
```shell
docker build -t django-template .
docker run -p 8000:8000 django-template python manage.py runserver 0.0.0.0:8000
```

## Using Docker compose
```shell
docker-compose up
```