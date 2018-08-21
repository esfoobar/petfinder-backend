# PetFinder Backend

API server for the PetFinder Application.

## Local MySQL server
- Create the application user and password:
    - Logon to MySQL using root user
    - Create the counter database `CREATE DATABASE petfinder;`
    - Give privileges to counter user `CREATE USER 'petfinder_user'@'%' IDENTIFIED BY 'petfinder_password';`  
    - Create the counter user `GRANT ALL PRIVILEGES ON petfinder.* TO 'petfinder_user'@'%';` and `FLUSH PRIVILEGES;`
- Create a virtualenv: `python3 -m venv venv`
- Activate the virtualenv: `source venv/bin/activate`
- Install the packages: `pip install -r requirements.txt`
- Run `flask db init` to initialize migrations
- Run `flask db migrate` and `flask db upgrade` to create tables
- Run `flask runserver`
- Open `http://localhost:5000` on your browser
- To open a shell, just do `flask shell`
- Run tests by doing `python tests.py`

## Using Docker
- Run `docker-compose up`
- In a new terminal or tab run:
    - `docker exec -it petfinder_web_1 flask db init` to initialize migrations
    - `docker exec -it petfinder_web_1 flask db migrate` and `docker exec -it petfinder_web_1 flask db upgrade` to create tables
- Open `http://localhost:5000` on your browser
- Run tests by doing `docker exec -it petfinder_web_1 python tests.py`

## Production
- Use Gunicorn `gunicorn wsgi:app --bind 0.0.0.0:$PORT --reload`
