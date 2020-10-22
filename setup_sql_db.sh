#!/usr/bin/env bash
# script to run setup of MySQL databases for ION main and testing

if [ "$#" -lt 1 ]; then
    echo "Usage: ./setup_sql_db.sh <password>"
    echo "<password> is the password for MySQL root user"
else
    cat sql_setup/config_mysql_main_db.sql | mysql -hlocalhost -uroot -p$1
    cat sql_setup/config_mysql_test_db.sql | mysql -hlocalhost -uroot -p$1
fi
