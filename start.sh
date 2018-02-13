#!/bin/bash

npm install
./node_modules/.bin/webpack --config webpack.config.js --watch
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata initial_data
python3 create_user.py
#DO we really need this?
cron
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000
