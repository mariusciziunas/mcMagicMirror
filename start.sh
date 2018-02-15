#!/bin/bash

#wget https://nodejs.org/dist/v8.5.0/node-v8.5.0-linux-armv7l.tar.xz
#tar -xvf node-v8.5.0-linux-armv7l.tar.xz
#cd node-v8.5.0-linux-armv7l
#cp -R * /usr/local/

curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  # Install NodeJS v8
sudo apt-get install -y nodejs  # npm nodejs-legacy #(Installed with nodesource)

npm install

./node_modules/.bin/webpack --config webpack.config.js
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py loaddata initial_data
python3 create_user.py
#DO we really need this?
cron
python3 manage.py crontab add
python3 manage.py runserver 0.0.0.0:8000
