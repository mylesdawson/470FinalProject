# Project Back-end


## Run with Docker:
```
docker-compose build && docker-compose up
```

## Run without Docker:

1) Get venv for python3: `sudo apt-get install python3-venv`. [Venv Primer](https://realpython.com/python-virtual-environments-a-primer/)
2) Create a new venv (somewhere outside of project folder): `python3 -m venv env`
3) Activate the venv (named 'env' here): `source env/bin/activate`. Deactivate venv: `deactivate`
4) Before installing dependencies into the venv install postgres: `sudo apt install postgresql postgresql-contrib libpq-dev`
5) You should no be able to access postgres: `sudo -u postgres psql`
6) Install dependencies: `pip3 install -r requirements.txt`
7) In settings.py 'DATABASES', change HOST to `'localhost'`
8) Create a superuser: `sudo -u postgres createuser -s -i -d -r -l -w project` && `sudo -u postgres psql -c "ALTER ROLE project WITH PASSWORD 'secret';"`
9) `sudo -u postgres psql` && `CREATE DATABASE project`
10) Apply database changes: `python3 manage.py makemigrations`, `python3 manage.py migrate`
11) Create a superuser (optional): `python manage.py createsuperuser`

11) Run the backend!: `python manage.py runserver 0.0.0.0:8080`

When updates to model occur:
1) May need to clear old migrations: in /migrations/ folder. See link below. May need to delete old project database and create new one.
2) `python manage.py makemigrations && python manage.py migrate`

## Useful Commands
`sudo docker ps`: list running docker instances and get container ids

`sudo docker exec -it <container_id> bash`: enter docker instance

`psql -U project`: access postgres db as user project


Admin user:
```
user: admin
password: testpassword
```

## Links and Resources

Django REST Framework: https://www.django-rest-framework.org/

If you run into migration problems, try Scenario 2 here: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
