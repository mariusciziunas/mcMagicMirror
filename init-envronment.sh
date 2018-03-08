#!/usr/bin/env bash

curl -sSL https://get.docker.com | sh
docker run --name root -e MYSQL_ROOT_PASSWORD=pass -d -p 3306:3306 -v ./app/mysql:/var/lib/mysql/ -e ON_CREATE_DB="newdatabase" mysql:latest