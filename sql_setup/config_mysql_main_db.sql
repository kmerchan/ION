-- This script sets up the database and user for ION main
-- User is identified by password and has privileges

CREATE DATABASE IF NOT EXISTS ion_main_db;
DROP USER IF EXISTS 'ion_main'@'localhost';
CREATE USER IF NOT EXISTS 'ion_main'@'localhost' IDENTIFIED BY 'ion_main_pwd';
GRANT ALL PRIVILEGES ON ion_main_db.* TO 'ion_main'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ion_main'@'localhost';
FLUSH PRIVILEGES;
