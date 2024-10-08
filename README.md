
## Getting started

### Build Docker file
```
docker-compose build
```




### To start project, run:
```
docker-compose up
```

The API will then be available at [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home).

### To Log in To the Dashboard(Frontend) or Admin Panel

#### Username
```
admin
```
#### Password
```
admin
```

---

## Development Guide

### Load Initial Data
```
docker-compose run --rm app sh -c "python manage.py load_initial_data"
```
```
docker-compose run --rm app sh -c "python manage.py generate_initial_super_user"
```

### Create Project
```
docker-compose run app sh -c "django-admin startproject app ."
```

### Create New App
```
docker-compose run app sh -c "python manage.py startapp core"
```
```
docker-compose run --rm app sh -c "python manage.py startapp task"
```

### Create Super User
```
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

### Make Migrations
```
docker-compose run app sh -c "python manage.py makemigrations"
```
