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
        """
        this method queries all or specific class from database
        returns dictionary of all objects
        """
        all_dict = {}
        # loops through known classes defined at the top of this module
        for class_name in classes:
            # if no class is specified or class matches (by cls parameter)
            if cls is None or cls == class_name:
                # queries all objects based on class
                objs = self.__session.query(classes[class_name]).all()
                # for each object, sets key and saves key with obj as value
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__,
                                         obj.id)
                    all_dict[key] = obj
        return (all_dict)

    def save(self):
        """ this method commits changes to current DB session """
        self.__session.commit()

    def new(self, obj=None):
        """ this method adds object to current DB session and saves """
        if obj is not None:
            # if object exists, adds it to current session
            self.__session.add(obj)
            # calls on save method to commmit recent add to save to database
            self.save()

    def delete(self, obj=None):
        """ this method deletes obj from current DB session and saves """
        if obj is not None:
            # if object exists, removes it from current session
            del obj
            # calls on save method to commit recent del to save to database
            self.save()

    def reload(self):
        """
        this method binds current engine to a scoped session
        connects current session to MySQL database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        this method closes the current session using method from Session class
        """
        self.__session.close()
