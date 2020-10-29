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
    id = Column(String(60),
                nullable=False,
                primary_key=True)
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False)
    name = Column(String(128),
                  nullable=False)

    def __init__(self, *args, **kwargs):
        """this method instantiates a new model from kwargs"""
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """this method returns a string representation of the instance"""
        return "[{}.{}] {}".format(self.__class__.__name__,
                                   self.id,
                                   self.__dict__)

    def to_dict(self):
        """
        returns dictionary representation of instance for JSON
        """
        dict_rep = {}
        # datetimes will be changed to ISO format
        time_format = datetime.isoformat
        # save each attribute in object dict to dict_rep
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_rep[key] = str(time_format(value))
            else:
                dict_rep[key] = value
        dict_rep["__class__"] = type(self).__name__
        return dict_rep

    def save(self):
        """ this method updates time of change then saves new info """
        self.updated_at = datetime.utcnow()
        from models import storage
        # storage.new method adds new obj and calls save() to commit changes
        storage.new(self)

    def delete(self):
        """ this method deletes current instance from DBStorage """
        from models import storage
        # storage.delete method removes obj and calls save() to commit changes
        storage.delete(self)
