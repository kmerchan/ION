#!/usr/bin/python3
""" this module builds DBStorage class from MySQLdb and SQLAlchemy"""
from models.base_model import BaseModel, Base
from models.identity import Identity
from models.profile import Profile
from models.skills import Skills
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
classes = {"Identity": Identity, "Profile": Profile, "Skills": Skills}


class DBStorage():
    """
    this module defines DBStorage class for interacting with MySQL tables
    private class attr: __engine, __session
    public instance methods: __init__, all, new, save, delete, reload
    """
    __engine = None
    __session = None

    def __init__(self):
        """ this method creates engine that links to MySQL database """
        # sets class variables from os environment variables set by user
        ION_MYSQL_HOST = getenv('ION_MYSQL_HOST')
        ION_MYSQL_USER = getenv('ION_MYSQL_USER')
        ION_MYSQL_PWD = getenv('ION_MYSQL_PWD')
        ION_MYSQL_DB = getenv('ION_MYSQL_DB')
        # creates the engine with above variables
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(
                                          ION_MYSQL_USER,
                                          ION_MYSQL_PWD,
                                          ION_MYSQL_HOST,
                                          ION_MYSQL_DB),
                                      pool_pre_ping=True)
        # gets environment variable to determine if testing or not
        # if testing, drops previous metadata
        ION_IS_TEST = getenv('ION_IS_TEST')
        if ION_IS_TEST == "true":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ this public instance method queries curent DB session """

    def new(self, obj):
        """ this public instance method adds object to current DB session """

    def save(self):
        """ this method commits changes to current DB session """

    def delete(self, obj=None):
        """ this public instance method deletes obj from current DB session """

    def reload(self):
        """
        this public instance method creates tables from current DB session,
        creates current DB session from the engine
        """
