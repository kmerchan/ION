#!/usr/bin/env bash
# Script to run program to input data to main ION database for deployment

# sets the following environmental variables to connect to main db:
# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_main
# ION_MYSQL_PWD=ion_main_pwd
# ION_MYSQL_DB=ion_main_db
# ION_IS_TEST=false

# sets variables and runs Python script to prompt developer for data to store
ION_MYSQL_HOST=localhost ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_DB=ion_main_db ION_IS_TEST=false ./insert_data.py
