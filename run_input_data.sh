#!/usr/bin/env bash
# Script to run program to input data to main ION database for deployment

# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_main
# ION_MYSQL_PWD=ion_main_pwd
# ION_MYSQL_DB=ion_main_db
# ION_IS_TEST=false

ION_MYSQL_HOST=localhost ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_DB=ion_main_db ION_IS_TEST=false ./insert_data.py
