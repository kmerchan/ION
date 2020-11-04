#!/usr/bin/env bash
# Script to run dynamically populating from back end with Flask

# sets the following environmental variables to connect to main db:
# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_main
# ION_MYSQL_PWD=ion_main_pwd
# ION_MYSQL_DB=ion_main_db
# ION_IS_TEST=false

# sets variables and runs Flask application
# (app runs from web_flask/flask_for_index.py)
ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_HOST=localhost ION_MYSQL_DB=ion_main_db ION_IS_TEST=false python3 -m web_flask.flask_for_index
