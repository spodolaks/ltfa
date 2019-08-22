#!/bin/bash

# Wait for postgress
while ! curl http://db:5432/ 2>&1 | grep '52'
do
    echo "Postgres is unavailable - sleeping"
    sleep 1
done
    # Install packages
    echo "Install packages"
    pip install -r ./requirements.txt

    # Apply database migrations
    echo "Apply database migrations"
    python ./manage.py migrate

    # Build static
    echo "Build static"
    cd ./static && npm install && npm run build && cd ../

    # Start server
    echo "Starting server"
    python ./manage.py runserver 0.0.0.0:8000
