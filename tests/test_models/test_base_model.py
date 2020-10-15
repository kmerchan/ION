#!/usr/bin/python3
"""
this module defines unit tests for BaseModel
testing functionality and documentation
"""
from datetime import datetime
from inspect import getmembers, isfunction
from models.base_model import BaseModel, __doc__ as base_model_doc
import pep8
from unittest import TestCase


class Test_BaseModel_Docs(TestCase):
    """
    defines tests to check documentation and style
    for BaseModel class
    """

    @classmethod
    def setUpClass(self):
        """
        uses inspect to get all methods to test for docstrings
        saves as base_methods attribute to call later
        """
        self.base_methods = getmembers(BaseModel, isfunction)

    def test_pep8_style(self):
        """
        tests that models/base_model.py
        and tests/test_models/test_base_model.py
        follows pep8 style guidelines
        """
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            # tests each path as a subTest for 0 pep8 errors
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0,
                                 "pep8 is returning errors for {}".
                                 format(path))

    def test_module_docstring(self):
        """
        tests that models.base_model module contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(base_model_doc, None,
                         "base_model module is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(base_model_doc) > 1,
                        "base_model module is missing docstring")

    def test_class_docstring(self):
        """
        tests that the BaseModel class contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(BaseModel.__doc__) > 1,
                        "BaseModel class is missing docstring")

    def test_method_docstrings(self):
        """
        tests that all methods in BaseModel have docstrings
        """
        for method in self.base_methods:
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


class Test_BaseModel(TestCase):
    """
    defines tests to check functionality
    of BaseModel class attributes and methods
    """

    def test_attribute_types(self):
        """
        tests the class attributes exist and are of correct type
        for BaseModel
        """
        # creates new instance of BaseModel
        instance = BaseModel()
        # tests that the new instance is of type BaseModel
        self.assertIs(type(instance), BaseModel)
        # adds name attribute
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        instance.name = "test_name"
        # attributes_dict sets up dictionary of attribute names and types
        attributes_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str
        }
        # loops through attributes_dict as subTests to check each attribute
        for attr, attr_type in attributes_dict.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                # tests the expected attribute is in the instance's dict
                self.assertIn(attr, instance.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(instance.__dict__[attr]), attr_type)
        # tests that the name attribute set earlier was set correctly
        self.assertEqual(instance.name, "test_name")
