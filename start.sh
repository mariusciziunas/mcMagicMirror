#!/bin/bash

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

npm install

./node_modules/.bin/webpack --config webpack.config.js
#pip3 install -r requirements.txt

python3 -m pip install django
python3 -m pip install mysqlclient
python3 -m pip install coreapi
python3 -m pip install tfl-api
python3 -m pip install pyicloud
python3 -m pip install zeep
python3 -m pip install django-crontab
python3 -m pip install django-webpack-loader
python3 -m pip install pigpio



python3 manage.py migrate
python3 manage.py loaddata initial_data
python3 create_user.py
#DO we really need this?
#cron
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000
