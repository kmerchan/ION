# Inclusive Oklahoma Network (ION)
ION is a public networking database and single page web application built to provide visibility and offer connections to Oklahoma STEM individuals from diverse backgrounds. The goal is for the ION site to help Oklahomans find relatable and reachable connections to local community leaders, fostering impactful relationships, mentoring, and role modeling to highlight STEM individuals from diverse backgrounds.

### Table of Contents
* [Website](##website)
* [ION Project Story](##ion)
* [Installation and Usage](##installation)
* [Database](##database)
* [Back-End File Descriptions](##back)
* [Front-End File Descriptions](##front)
* [Bugs](###bugs)
* [Authors](##authors)
* [Upcoming Features](##upcoming)
* [Licensing](##licensing)

## Website
Please visit the ION website at [www.inclusiveok.tech](http://www.inclusiveok.tech) to build diversity in Oklahoma STEM through visibility and connection!
<img src="https://i.ibb.co/17FFwNx/Screenshot-2020-10-22-at-1-17-56-PM.png" alt="ION website" border="0">

If you would like to add your profile information to the website, please fill out this [sign up form](https://forms.gle/Jp9YPVPZgxaS7ZAXA) and your profile will be created and added for others to connect with you.  Thank you!

## ION Project Story
This ION project stems from the passion authors Kelsie and Staci have for building a strong culture of Diversity, Inclusion, Equity, and Belonging at Holberton Tulsa and within their local community. Kelsie and Staci identify as two of the four women in Holberton Tulsa's first cohort of coding students, and Staci also identifies as a proud legally married queer woman. Driven by their personal experiences and research into why diversity gaps persist in STEM (Science, Technology, Engineering, and Mathematics), Kelsie and Staci decided to develop the Inclusive Oklahoma Network (ION) as a public network to foster connections and highlight diverse STEM professionals and upcoming talent. While other organizations may have their own directories, ION is open and available for anyone to access without having to pay dues or be an existing member. ION helps young professionals build their network as they explore their areas of interest and helps STEM-adjacent community members, such as teachers or non-profits, easily connect with STEM leaders their students or audience can identify with. The goal is to make it as simple as possible for local Oklahoma communities to find diverse STEM role models, peers, and mentors through reducing barriers in networking and hiring. Additionally, ION helps to increase retention through building a community that supports STEM individuals throughout their career. Imposter syndrome leads many STEM individuals to feel they cannot keep up with the curriculum and leave. While imposter syndrome can affect anyone, it is felt more often by those that already feel like an only in their classes, school, and community. ION helps to build tangible connections where users can hear from others in the community with shared experiences, helping them feel less alone and allowing shared advice on overcoming obstacles.

For more information on the inspiration for ION or how the ION project came to be, please check out these blogs by the ION authors:

[Kelsie Merchant's project blog post](https://www.linkedin.com/pulse/ion-project-kelsie-merchant/)

[Staci Aaenson-Fletcher's project blog post](https://www.linkedin.com/pulse/inclusive-oklahoma-network-staci-aaenson-fletcher-she-her-/)

## Installation and Usage
If you are hoping to access and utilize the ION site as a user, please visit [www.inclusiveok.tech](http://www.inclusiveok.tech) to access the website in your browser. However, if you are trying to run the source code for the project, please follow these installation and usage steps to configure your web server:
### Server Configuration:
* First, access your own server to host the site.  The ION project is hosted on Google Cloud Platform (GCP) Compute Engine Virtual Machine (VM).
* Install Nginx web server with the following commands:
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
* Install Flask and Flask_CORS to dynamically render HTML based on current database with the following commands:
  * `pip3 install Flask`
  * `pip3 install flask_cors`
* Install Gunicorn application server with the following commands:
  * `pip3 install gunicorn flask`

### Usage:
* To access the source code, `git clone` this repository onto your web server and use `cd` to move into the repository
* To set up MySQL databases and users, please run the Bash script [setup_sql_db.sh](/setup_sql_db.sh) with the password for the root user for MySQL
  * `./setup_sql_db.sh <password>`
  * This script runs configuration files, [config_mysql_main_db.sql](/sql_setup/config_mysql_main_db.sql) and [config_mysql_test_db.sql](/sql_setup/config_mysql_test_db.sql), to configure database for main ION data and for testing ION code.
* To run unit tests for the source code, please run the Bash script [run_tests.sh](/run_tests.sh)
  * This script sets all testing environment variables and runs unit tests.
  * To run all unit tests: `./run_tests.sh`
  * To run specific test file: `./run_tests.sh <path to test file>`
* To run the web content dynamically, please run the Bash script [run_bind_gunicorn.sh](/run_bind_gunicorn.sh)
  * This script sets all envrionment variables to connect to the main ION database for deployment.
  * The script also binds the Flask application from [web_flask.flask_for_index](/web_flask/flask_for_index.py) to the Gunicorn application server.

### Contributing:
If you would like to contribute to the ION project, please contact authors Kelsie and Staci.

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
  * `def to_dict(self)` method - public instance method that returns the dictionary representation of the instance
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
  * `def get(self, cls=None, id=None)` - public instance method to retrieve specific object by class name and id from current database
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
Kelsie Merchant - [GitHub](https://github.com/kmerchan/) / [email: kelsie.merchant@holbertonschool.com](kelsie.merchant@holbertonschool.com) / [LinkedIn](https://www.linkedin.com/in/kelsie-merchant-physics/)

Staci Aaenson-Fletcher - [GitHub](https://github.com/StaciAF) / [email: staci.aaensonfletcher@holbertonschool.com](staci.aaensonfletcher@holbertonschool.com) / [LinkedIn](https://www.linkedin.com/in/staci-aaenson-fletcher/)

## Upcoming Features
We are currently working on making the website more dynamic to allow users to search by filters.  We are adding Javascript and jQuery to listen for user clicks and will utilize the API routes found in /api/views/ to re-populate the profile cards based on how the user is filtering results.

Please check back to see more features currently in development.

## Related Projects
This project is the culmination of technical project-based learning, especially higher-level langauges, such as Python, MySQL databases, HTML and CSS, and web deployment.  For related projects, please check out Kelsie and Staci's individual GitHub repositories.

## Licensing
Public Domain. No copy write protection.
