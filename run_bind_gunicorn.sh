#!/usr/bin/env bash
# Script to bind gunicorn instance to Flask app from flask_for_index

# sets the following environmental variables to connect to main db:
# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_main
# ION_MYSQL_PWD=ion_main_pwd
# ION_MYSQL_DB=ion_main_db
# ION_IS_TEST=false
# ION_API_HOST=0.0.0.0
# ION_API_PORT=5000

# sets variables and binds gunicorn instance to Flask application
# Flask app found in web_flask/flask_for_index.py
ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_HOST=localhost ION_MYSQL_DB=ion_main_db ION_IS_TEST=false ION_API_HOST=0.0.0.0 ION_API_PORT=5000 tmux new-session -d 'gunicorn --bind 127.0.0.1:5000 web_flask.flask_for_index:app'

# sets variables and binds gunicorn instance to API application
# API app found in api/app.py
# commented out because not currently in use
# API app will be used for Javascript and jQuery for web dynamic
# ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_HOST=localhost ION_MYSQL_DB=ion_main_db ION_IS_TEST=false ION_API_HOST=0.0.0.0 ION_API_PORT=5000 tmux new-session -d 'gunicorn --bind 0.0.0.0:5001 api.app:app'
