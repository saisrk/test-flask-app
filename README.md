# test-flask-app

Just a simple CRUD app in flask for learning the beginning of flask.

# Use the app

1. Clone the repository
2. Run following commands

docker-compose up --build -d

# Initialise db
docker-compose exec testapp python manage.py db init

# First Migration
docker-compose exec testapp python manage.py db migrate
docker-compose exec testapp python manage.py db upgrade

# Seed the database to get initial data
docker-compose exec testapp python manage.py seed_db


# To run in local
python manage.py run

Note: If in local make sure you have postgresql running.


Docker creates 3 containers

APP container : testapp
DB container : testapp-db (postgresql)
NGINX container : nginx


API that can be used


GET: localhost/ping
GET: localhost/users
GET: localhost/users/<id>

POST: localhost/users
 {
   "name": "foo"
   "email": "email"
  }
  
PUT: localhost/users
 {
   "name": "foo"
   "email": "email"
  }
