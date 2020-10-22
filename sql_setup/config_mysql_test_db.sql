-- This script sets up the database and user for ION testing
-- User is identified by password and has privileges

CREATE DATABASE IF NOT EXISTS ion_test_db;
DROP USER IF EXISTS 'ion_test'@'localhost';
CREATE USER IF NOT EXISTS 'ion_test'@'localhost' IDENTIFIED BY 'ion_test_pwd';
GRANT ALL PRIVILEGES ON ion_test_db.* TO 'ion_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'ion_test'@'localhost';
FLUSH PRIVILEGES;
