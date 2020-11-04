#!/usr/bin/env bash
# Script to run unit tests with test db environment variables set

# sets the following environmental variables to connect to test db:
# ION_MYSQL_HOST=localhost
# ION_MYSQL_USER=ion_test
# ION_MYSQL_PWD=ion_test_pwd
# ION_MYSQL_DB=ion_test_db
# ION_IS_TEST=true

if [ $# -eq 1 ]; then
    # if path to specific test is provided,
    # sets variables and runs unittest with path to test
    ION_MYSQL_HOST=localhost ION_MYSQL_USER=ion_test ION_MYSQL_PWD=ion_test_pwd ION_MYSQL_DB=ion_test_db ION_IS_TEST=true python3 -m unittest $1
else
    # if no specific test specified,
    # sets variables and runs discover tests to run all tests
    ION_MYSQL_HOST=localhost ION_MYSQL_USER=ion_test ION_MYSQL_PWD=ion_test_pwd ION_MYSQL_DB=ion_test_db ION_IS_TEST=true python3 -m unittest discover tests
fi
