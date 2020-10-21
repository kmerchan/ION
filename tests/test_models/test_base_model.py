#!/usr/bin/python3
"""
this module defines unit tests for BaseModel
testing functionality and documentation
"""
from datetime import datetime
from inspect import getmembers, isfunction
from models.base_model import BaseModel, __doc__ as base_model_doc
import pep8
from time import sleep
from unittest import TestCase


class Test_BaseModel_Docs(TestCase):
    """
    defines tests to check documentation and style
    for BaseModel module, class, and methods
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
        also tests instantiation of new object without kwargs
        """
        # creates new instance of BaseModel
        new_obj = BaseModel()
        # tests that the new instance is of type BaseModel
        self.assertIs(type(new_obj), BaseModel)
        # adds name attribute
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
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
                self.assertIn(attr, new_obj.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(new_obj.__dict__[attr]), attr_type)

    def test_uuid_attribute(self):
        """
        tests the uuid attribute id for format
        """
        # creates two new instances of BaseModel
        new_obj1 = BaseModel()
        new_obj2 = BaseModel()
        # tests that the objects' ids are unique
        self.assertNotEqual(new_obj1.id, new_obj2.id)
        for obj in [new_obj1, new_obj2]:
            # tests each object id for correct uuid format
            self.assertRegex(obj.id,
                             '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-'
                             '[0-9a-f]{4}-[0-9a-f]{12}$')

    def test_datetime_attributes(self):
        """
        tests the datetime attributes created_at and updated_at
        """
        # creates new instance, getting timestamps before and after
        first_time = datetime.now()
        new_obj1 = BaseModel()
        second_time = datetime.now()
        # tests if object's created_at time is between timestamps
        self.assertTrue(first_time <= new_obj1.created_at <= second_time)
        # tests if object's updated_at is within the same timestamps
        self.assertTrue(first_time <= new_obj1.updated_at <= second_time)
        # saves instance of BaseModel, getting timestamp of updated_at before
        original_updated_at = new_obj1.updated_at
        sleep(1)
        new_obj1.save()
        # tests that the object's updated_at has changed and is later
        self.assertNotEqual(original_updated_at, new_obj1.updated_at)
        self.assertTrue(original_updated_at < new_obj1.updated_at)
        # creates another instance, getting timestamps before and after
        sleep(1)
        third_time = datetime.now()
        new_obj2 = BaseModel()
        fourth_time = datetime.now()
        # tests if object's created_at time is between timestamps
        self.assertTrue(third_time <= new_obj2.created_at <= fourth_time)
        # tests if object's updated_at is within the same timestamps
        self.assertTrue(third_time <= new_obj2.updated_at <= fourth_time)
        # tests that new_obj1 and new_obj2 have different times
        self.assertNotEqual(new_obj1.created_at, new_obj2.created_at)
        self.assertNotEqual(new_obj1.updated_at, new_obj2.updated_at)
        self.assertTrue(new_obj1.created_at < new_obj2.created_at)
        self.assertTrue(new_obj1.updated_at < new_obj2.updated_at)

    def test_init_method(self):
        """
        tests the __init__ method for instantiating new objects
        both new and from kwargs
        """
        # creates new instance of BaseModel
        new_obj1 = BaseModel()
        # tests that the new object is of type BaseModel
        self.assertIs(type(new_obj1), BaseModel)
        # adds name attribute
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj1.name = "test_name"
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
                # tests the expected attribute is in the object's dict
                self.assertIn(attr, new_obj1.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(new_obj1.__dict__[attr]), attr_type)
        # sets kwargs using object's dict and uses to create new object
        kwargs = new_obj1.__dict__
        new_obj2 = BaseModel(**kwargs)
        # tests that the new object is of type BaseModel
        self.assertIs(type(new_obj2), BaseModel)
        # loops through attributes_dict as subTests to check each attribute
        for attr, attr_type in attributes_dict.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                # tests the expected attribute is in the object's dict
                self.assertIn(attr, new_obj2.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(new_obj2.__dict__[attr]), attr_type)
                # tests the value of name attribute matches the original object
                self.assertEqual(new_obj1.__dict__[attr],
                                 new_obj2.__dict__[attr])

        # tests that __class__ is not set in object 2
        self.assertNotIn('__class__', new_obj2.__dict__)

    def test_str_method(self):
        """
        tests the __str__ method returns the correct format
        """
        # creates new instance of BaseModel and saves variables
        new_obj = BaseModel()
        obj_id = new_obj.id
        obj_dict = new_obj.__dict__
        # tests the string representation of object is formatted correctly
        self.assertEqual(str(new_obj),
                         "[BaseModel.{}] {}".format(obj_id, obj_dict))

    def test_save_method(self):
        """
        tests the save method changes the update_at time and saves to database
        """
