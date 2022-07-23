# Constricon

Online contructor of icons

## Launch

You need installed [docker compose](https://docs.docker.com/compose/install/) for project to launch. After installation run following command 
```
docker compose up --build
```
Add `-d` flag to run it detached.

## Superuser creation

To create superuser run following command 
```
docker compose exec backend python manage.py createsuperuser
```

## API documentation

If project is ran locally, swagger documentation should be accessible on http://127.0.0.1:8080/swagger/
