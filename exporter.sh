export DOCKER_HOST="tcp://172.17.0.1:2376"
python3.12 -m pip install manimlib
python3.12 -m pip install manimce


django-admin startproject ai_ro .
django-admin startapp ai_app
python manage.py migrate
python manage.py makemigrations
python manage.py createuser
python manage.py runserver
python manage.py runserver


sudo apt-get install python3.10-dev python3.10-venv