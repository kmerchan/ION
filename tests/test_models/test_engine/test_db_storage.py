#!/usr/bin/python3
"""
this module defines unit tests for DBStorage class
testing functionality and documentation
"""
from datetime import datetime
from inspect import getmembers, isfunction
from models import storage
from models.base_model import BaseModel
from models.identity import Identity
from models.profile import Profile
from models.skills import Skills
from models.engine.db_storage import DBStorage, __doc__ as db_storage_doc
import pep8
from time import sleep
from unittest import TestCase
classes = {"Identity": Identity, "Profile": Profile, "Skills": Skills}


class Test_DBStorage_Docs(TestCase):
    """
    defines tests to check documentation and style
    for DBStorage module, class, and methods
    """

    @classmethod
    def setUpClass(self):
        """
        uses inspect to get all methods to test for docstrings
        saves as storage_methods attribute to call later
        """
        self.storage_methods = getmembers(DBStorage, isfunction)

    def test_pep8_style(self):
        """
        tests that models/engine/db_storage.py
        and tests/test_models/test_engine/test_db_storage.py
        follows pep8 style guidelines
        """
        for path in ['models/engine/db_storage.py',
                     'tests/test_models/test_engine/test_db_storage.py']:
            # tests each path as a subTest for 0 pep8 errors
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0,
                                 "pep8 is returning errors for {}".
                                 format(path))

    def test_module_docstring(self):
        """
        tests that models.engine.db_storage module contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(db_storage_doc, None,
                         "db_storage module is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(db_storage_doc) > 1,
                        "db_storage module is missing docstring")

    def test_class_docstring(self):
        """
        tests that the DBStorage class contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(DBStorage.__doc__) > 1,
                        "DBStorage class is missing docstring")

    def test_method_docstrings(self):
        """
        tests that all methods in DBStorage have docstrings
        """
        for method in self.storage_methods:
            # tests each method as a subTest for missing docstrings
            with self.subTest(method=method):
                # first tests if docstring is not None
                self.assertIsNot(method[1].__doc__, None,
                                 "{} method is missing docstring".
                                 format(method[0]))
                # then tests if there is at least 1 docstring
                self.assertTrue(len(method[1].__doc__) > 1,
                                "{} method is missing docstring".
                                format(method[0]))


class Test_DBStorage(TestCase):
    """
    defines tests to check functionality
    of DBStorage class attributes and methods
    """

    def test_save_method(self):
        """
        tests the save method changes the update_at time and saves to database
        """
