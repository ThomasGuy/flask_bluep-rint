# A Skeletom Flask dev enviroment

To be run inside WSL.

python3.8 -m venv env

source env/bin/activate

pip install -r requirements.txt

## Initialize Database
if not already initialized delete migrations folder...
flask db init

flask db migrate -m "initialize"

flask db upgrade

## Gunicorn

gunicorn --bind 0.0.0.0:5000 wsgi:app

## Flask

flask run
