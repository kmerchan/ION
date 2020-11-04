#!/usr/bin/python3
""" this module builds BaseModel class """
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
Base = declarative_base()


class BaseModel():
    """ this module defines BaseModel to be inherited by all classes """
    # creates required column in MySQL table, uses PrimaryKey to set unique id
    id = Column(String(60),
                nullable=False,
                primary_key=True)
    # creates required column in MySQL table, uses datetime to set current time
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    # creates required column in MySQL table, uses datetime to set current time
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    # creates required column in MySQL table, user must input name attribute
    name = Column(String(128),
                  nullable=False)

    def __init__(self, *args, **kwargs):
        """this method instantiates a new model from kwargs"""
        if kwargs:
            # initializes object based on key-word arguments
            # skips over __class__, should be set when new object created
            if '__class__' in kwargs:
                del kwargs['__class__']
            # if required attribute is not in kwargs, it's automatically set
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            # updates the object based on what is in kwargs
            self.__dict__.update(kwargs)
        else:
            # initializes object for without kwargs
            # automatically sets required attributes
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """this method returns a string representation of the instance"""
        # string rep based on object class and id in brackets and dict
        return "[{}.{}] {}".format(self.__class__.__name__,
                                   self.id,
                                   self.__dict__)

    def to_dict(self):
        """
        returns dictionary representation of instance for JSON
        """
        # starts with empty dictionary
        dict_rep = {}
        # datetimes will be changed to ISO format
        time_format = datetime.isoformat
        # save each attribute in object dict to dict_rep
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                # updates time format for datetime attributes
                dict_rep[key] = str(time_format(value))
            else:
                # otherwise, sets key, value directly
                dict_rep[key] = value
        # adds class name attribute to dictionary
        dict_rep["__class__"] = type(self).__name__
        # if the object instance state is in dict, removes it
        # removing allows API calls to be able to jsonify this to_dict return
        if "_sa_instance_state" in dict_rep:
            del dict_rep["_sa_instance_state"]
        # returns objects dictionary representation
        return dict_rep

    def save(self):
        """ this method updates time of change then saves new info """
        # re-sets the updated_at time with current time
        self.updated_at = datetime.utcnow()
        from models import storage
        # storage.new method adds new obj and calls save() to commit changes
        storage.new(self)

    def delete(self):
        """ this method deletes current instance from DBStorage """
        from models import storage
        # storage.delete method removes obj and calls save() to commit changes
        storage.delete(self)
