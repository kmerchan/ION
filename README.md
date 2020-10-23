# Inclusive Oklahoma Network (ION)
INSERT PROJECT OVERVIEW/DESCRIPTION

### Table of Contents
* [Website](##website)
* [Installation and Usage](##installation)
* [Database](##database)
* [Back-End File Descriptions](##back)
* [Front-End File Descriptions](##front)
* [Bugs](###bugs)
* [Authors](##authors)
* [Upcoming Features](##upcoming)

## Website
Please visit the ION website [here](http://34.121.53.105/) to build diversity in Oklahoma STEM through visibility and connection!
<img src="https://i.ibb.co/17FFwNx/Screenshot-2020-10-22-at-1-17-56-PM.png" alt="ION website" border="0">

If you would like to add your profile information to the website, please fill out this [sign up form](https://forms.gle/Jp9YPVPZgxaS7ZAXA) and your profile will be created and added for others to connect with you.  Thank you!

## Installation and Usage
If you are hoping to access and utilize the ION site as a user, please click on the link above to access the website in your browser. However, if you are trying to run the source code for the project, please follow these installation and usage steps to configure your web server:
### Web Server Configuration:
* First, access your own server to host the site.  The ION project is hosted on Google Cloud Platform (GCP) Compute Engine Virtual Machine (VM).
* Install Nginx with the following commands:
  * `sudo apt-get -y update`
  * `sudo apt-get -y install nginx`
  * `sudo emacs /var/www/html/index.html` and type content
  * `sudo service nginx restart`
  * You can check configuration by looking at your server's IP address in the browser - the page should show the content you typed into the configuration file
* Install MySQL for database with the following commands:
  * `sudo apt-get -y update`
  * `sudo apt-get -y install mysql-server-5.7`
  * You can check MySQL installed with `mysql --version`
* Install pip3 and pep8 for Python3 with the following commands:
  * Note: Python3 was already installed as part of the GCP Compute Engine set-up, please manually install Python3 if you are using your own server.
  * `sudo apt-get -y install python3-pip`
  * `sudo pip3 install -lv pep8==1.7.0`
* Install MySQLdb for database interaction with the following commands:
  * `sudo apt-get install python3-dev`
  * `sudo apt-get install libmysqlclient-dev`
  * `sudo apt-get install zlib1g-dev`
  * `sudo pip3 install mysqlclient==1.3.10`
* Install SQLAlchemy for database Object Relational Mapping (ORM) with the following commands:
  * `pip3 install SQLAlchemy==1.2.5`

### Usage:
* To access the source code, `git clone` this repository onto your web server and use `cd` to move into the repository
* To set up MySQL databases and users, please run the Bash script [setup_sql_db.sh](/setup_sql_db.sh) with the password for the root user for MySQL
  * `./setup_sql_db.sh <password>`
  * This script runs configuration files, [config_mysql_main_db.sql](/sql_setup/config_mysql_main_db.sql) and [config_mysql_test_db.sql](/sql_setup/config_mysql_test_db.sql), to configure database for main ION data and for testing ION code.
* To run unit tests for the source code, please run the Bash script [run_tests.sh](/run_tests.sh)
  * This script sets all testing environment variables and runs unit tests.
  * To run all unit tests: `./run_tests.sh`
  * To run specific test file: `./run_tests.sh <path to test file>`

## Database
This project utilizes MySQL to store and maintain the database with three primary tables and two secondary tables:

#### `profiles` Table
| `id` | `created_at` | `updated_at` | `name` | `email` | `password` | `company_school_name` | `about_me` | `linkedin` | `social_media` | `skills` | `identities` |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PrimaryKey for unique ID | datetime for when data was created | datetime for when data was last updated | user's name | user's email address | user's password | name of the user's company or school | brief personal bio about the user | link to the user's LinkedIn page | link to user's other social media accounts | list of areas the user has knowledge in | list of diverse identities the user relates to |

#### `identities` Table
| `id` | `created_at` | `updated_at` | `name` |
|---|---|---|---|
| PrimaryKey for unique ID | datetime for when data was created | datetime for when data was last updated | personal identity name |

#### `skills` Table
| `id` | `created_at` | `updated_at` | `name` |
|---|---|---|---|
| PrimaryKey for unique ID | datetime for when data was created | datetime for when data was last updated | skill name |

`profile_skills` and `profile_identities` are secondary tables to establish the relationships between user profile and their skills or user profile and their identities

## Back-End File Descriptions
#### `models/` directory contains all model classes used to establish tables for MySQL database
[\_\_init\_\_.py](/models/__init__.py) - establishes instance of storage which is populated from current database with reload method

[base_model.py](/models/base_model.py) - defines the BaseModel class from which all other classes inherit from
* BaseModel Class:
  * `id` class attribute - each unique row of data can be identified by a unique id number
  * `created_at` class attribute - datetime attribute to keep track of when data is added
  * `updated_at` class attribute - datetime attribute to keep track of when data is changed
  * `name` class attribute - each row can also be identified by the object's name
  * `def __init__(self, *args, **kwargs)` method - public instance method that instantiates new instances of the class
  * `def __str__(self)` method - public instance method that returns the string representation of the instance
  * `def save(self)` method - public instance method that re-sets updated_at attribute and calls database storage engine method to add and commit the instance to the MySQL tables
  * `def delete(self)` method - public instance method that calls database storage method to remove and commit the instance to the MySQL tables


Subclasses of Base Model:
* [identity.py](/models/identity.py)
* [profile.py](/models/profile.py)
* [skills.py](/models/skills.py)

[identity.py](/models/identity.py) - defines the Identity class to keep track of data for all diverse identities
* Identity Class:
  * `__tablename__` attribute - class attribute that establishes the tablename to link to in MySQL

[profile.py](/models/profile.py) - defines the Profile class to keep track of all of data for all user profiles; defines secondary tables for relationship between Profile objects and Identity objects and relationship between Profile objects and Skills objects
* `profile_skills` - MySQL table to establish Many-to-Many relationship between Profile objects and Skills objects through ForeignKeys
* `profile_identities` - MySQL table to establish Many-to-Many relationship between Profile objects and Identity objects through ForeignKeys
* Profile Class:
  * `__tablename__` attribute - class attribute that establishes the tablename to link to in MySQL
  * `email` class attribute - user's contact email address (required)
  * `password` class attribute - user's password (optional, until we add feature to be able to manage login information)
  * `company_school_name` class attribute - information about where the user works/learns (optional)
  * `about_me` class attribute - brief description about the user about who they are and why they are using the site (optional)
  * `linkedin` class attribute - link to user's LinkedIn page (optional)
  * `social_media` class attribute - any additional social media links the user wants to add (optional)
  * `skill` relationship - calls on Skills class and secondary table `profile_skills` to define relationship
  * `identities` relationship - calls on Identity class and secondary table `profile_identities`to define relationship

[skills.py](/models/skills.py) - defines the Skills class to keep track of data for all types of skills
* Skills Class:
  * `__tablename__` attribute - class attribute that establishes the tablename to link to in MySQL

##### `/models/engine` directory contains the database storage engine class used to establish a connection between the Python class objects and MySQL Database
[db_storage.py](/models/engine/db_storage.py) - defines the DBStorage class that creates storage engine for session that connects to MySQL tables
* DBStorage Class:
  * `__engine` private class attribute - engine that connects to current MySQL database
  * `__session` private class attribute - binds the session to the engine for Object Relational Mapping (ORM)
  * `def __init__(self)` - public instance method to initialize new storage engine using MySQL user and database information from environment variables
  * `def all(self, cls=None)` - public instance method to query all or specific class of objects from the current database
  * `def save(self)` - public instance method to commit any changes from the current database session to MySQL database
  * `def new(self, obj=None)` - public instance method to add new object to the current database session and calls save method to commit to database
  * `def delete(self, obj=None)` - public instance method to remove object from the current database session and calls save method to commit to database
  * `def reload(self)` - public instance method to bind the session to the engine
  * `def close(self)` - public instance method to close the current session

#### `tests` directory contains all unit tests for the back-end
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - tests documentation and functionality of BaseModel class

[/test_models/test_identity.py](/tests/test_models/test_identity.py) - tests documentation and functionality of Identity class

[/test_models/test_profile.py](/tests/test_models/test_profile.py) - tests documentation and functionality of Profile class

[/test_models/test_skills.py](/tests/test_models/test_skills.py) - tests documentation and functionality of Skills class

[/test_models/test_engine/test_db_storage.py](/tests/test_models/test_enginge/test_db_storage.py) - tests documentation and functionality of DBStorage class, including if objects are correctly stored in MySQL database

## Front-End File Descriptions
#### `web` directory contains all HTML and CSS content for website structure and style
[index.html](/web/index.html) - HTML file to provide visual structure of web app

##### `web/styles` directory contains all CSS file references
[common.css](/web/styles/common.css) - CSS file to provide styling of web page

[footer.css](/web/styles/footer.css) - CSS file to provide styling for footer of web page

### Bugs
No known bugs at this time. Please contact authors Kelsie or Staci if you find a bug.

## Authors
Kelsie Merchant - [GitHub](https://github.com/kmerchan/) / [email: kelsie.merchant@holbertonschool.com](kelsie.merchant@holbertonschool.com)

Staci Aaenson-Fletcher - [GitHub](https://github.com/StaciAF) / [email: staci.aaensonfletcher@holbertonschool.com](staci.aaensonfletcher@holbertonschool.com)

## Upcoming Features
We are currently working on making the website more dynamic to allow users to search by filters.

Please check back to see more features currently in development.
