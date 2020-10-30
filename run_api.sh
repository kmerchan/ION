#!/usr/bin/env bash
# Script to run api

# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_main
# ION_MYSQL_PWD=ion_main_pwd
# ION_MYSQL_DB=ion_main_db
# ION_IS_TEST=false
# ION_API_HOST=0.0.0.0
# ION_API_PORT=5000

ION_MYSQL_USER=ion_main ION_MYSQL_PWD=ion_main_pwd ION_MYSQL_HOST=localhost ION_MYSQL_DB=ion_main_db ION_IS_TEST=false ION_API_HOST=0.0.0.0 ION_API_PORT=5000 python3 -m api.app
