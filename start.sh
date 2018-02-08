#!/bin/bash

pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata initial_data
python3 create_user.py
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000
