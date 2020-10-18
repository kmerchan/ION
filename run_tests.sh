#!/usr/bin/env bash
# Script to run unit tests with test db environment variables set

ION_MYSQL_HOST=localhost
ION_MYSQL_USER=ion_test
ION_MYSQL_PWD=ion_test_pwd
ION_MYSQL_DB=ion_test_db
ION_IS_TEST=true
if [ $# -eq 1 ]; then
    python3 -m unittest $1
else
    python3 -m unittest discover tests
fi
