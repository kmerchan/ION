#!/usr/bin/python3
""" this module builds DBStorage class from MySQL DB """


class DBStorage:
    """
    this module defines DBStorage class
    private class attr: __engine, __session
    public instance methods: __init__, all, new, save, delete, reload
    """
    __engine = None
    __session = None

    def __init__(self):
        """ public instance method to create engine and link to DB """

    def all(self, cls=None):
        """ this public instance method queries curent DB session """

    def new(self, obj):
        """ this public instance method adds object to current DB session """

    def save(self):
        """ this public instance method commits changes to current DB session """

    def delete(self, obj=None):
        """ this public instance method deletes obj from current DB session """

    def reload(self):
        """
        this public instance method creates tables from current DB session,
        creates current DB session from the engine
        """
