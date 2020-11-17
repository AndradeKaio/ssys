## Requirements
- [Python 3.8](https://www.python.org/downloads/)
- [Django 3.1](https://www.djangoproject.com/)
- [Pip](https://pip.pypa.io/en/stable/)

or

- [Docker 18.0+](https://www.docker.com/get-started)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
$ pip install -r requirements.txt
```
Run migrations

```bash 
$ python manage.py makemigrations api
$ python manage.py migrate
$ python manage.py createuser
```


**Seed the database** (Optional)

```bash
$ python manage.py loaddata employee.json
```

Run the debug server
```bash
$ python manage.py runserver
```

[http://localhost:8000/](http://localhost:8000/)

## Using Docker
Build and run the application using [docker](https://www.docker.com/get-started).
```bash
$ docker-compose build && sudo docker-compose up -d
```
[http://localhost:8000/](http://localhost:8000/)


**User**
user: `ssys`
password: `password`


## Structure

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`employees` | GET | READ | Get all employees
`employees`| POST | CREATE | Create a new employee
`employees/:id` | GET | READ | Get a single employee
`employees`| POST | UPDATE | Updates a employee
`employees/:id` | DELETE | DELETE | Delete a employee
`/reports/employees/salary/` | GET | READ | Get salary report
`/reports/employees/age/` | GET | READ | Get age report

## Testing

You can test using any http client, but there is a [postman](https://www.postman.com/) collection with some tests right [here](/util/ssys.postman_collection.json).

## Production
Access the API in production on Heroku [here](https://ssysapi.herokuapp.com/)

## Contact
deandradekaio@gmail.com

