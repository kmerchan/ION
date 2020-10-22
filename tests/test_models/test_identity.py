#!/usr/bin/python3
"""
this module defines unit tests for Identity
testing functionality and documentation
"""
from datetime import datetime
from inspect import getmembers, isfunction
from models.base_model import BaseModel
from models.identity import Identity, __doc__ as identity_doc
import pep8
from time import sleep
from unittest import TestCase, mock


class Test_Identity_Docs(TestCase):
    """
    defines tests to check documentation and style
    for Identity module, class, and methods
    """

    @classmethod
    def setUpClass(self):
        """
        uses inspect to get all methods to test for docstrings
        saves as identity_methods attribute to call later
        """
        self.identity_methods = getmembers(Identity, isfunction)

    def test_pep8_style(self):
        """
        tests that models/identity.py
        and tests/test_models/test_identity.py
        follows pep8 style guidelines
        """
        for path in ['models/identity.py',
                     'tests/test_models/test_identity.py']:
            # tests each path as a subTest for 0 pep8 errors
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0,
                                 "pep8 is returning errors for {}".
                                 format(path))

    def test_module_docstring(self):
        """
        tests that models.identity module contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(identity_doc, None,
                         "identity module is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(identity_doc) > 1,
                        "identity module is missing docstring")

    def test_class_docstring(self):
        """
        tests that the Identity class contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(Identity.__doc__, None,
                         "Identity class is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(Identity.__doc__) > 1,
                        "Identity class is missing docstring")

    def test_method_docstrings(self):
        """
        tests that all methods in Identity have docstrings
        """
        for method in self.identity_methods:
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


class Test_Identity(TestCase):
    """
    defines tests to check functionality
    of Identity class attributes and methods
    """

    def test_class_and_subclass(self):
        """
        tests that instances are of Identity class
        and are a subclass of BaseModel class
        """
        new_obj = Identity()
        # tests that the new instance is of type Identity
        self.assertIs(type(new_obj), Identity)
        # tests that the new instance is a subclass of BaseModel
        self.assertIsInstance(new_obj, BaseModel)

    def test_attribute_types(self):
        """
        tests the class attributes exist and are of correct type
        also tests instantiation of new object
        """
        # creates new instance of Identity
        new_obj = Identity()
        # adds name attribute (inherited requirement from BaseModel)
        # adds optional attributes for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # attributes_dict sets up dictionary of attribute names and types
        attributes_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
        }
        # loops through attributes_dict as subTests to check each attribute
        for attr, attr_type in attributes_dict.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                # tests the expected attribute is in the instance's dict
                self.assertIn(attr, new_obj.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(new_obj.__dict__[attr]), attr_type)

    def test_updated_datetime_attributes(self):
        """
        tests that the datetime attribute updated_at changes
        when the save() method is implemented
        """
        first_time = datetime.now()
        new_obj = Identity()
        second_time = datetime.now()
        # tests if object's created_at time is between timestamps
        self.assertTrue(first_time <= new_obj.created_at <= second_time)
        # tests if object's updated_at is within the same timestamps
        self.assertTrue(first_time <= new_obj.updated_at <= second_time)
        # gets timestamps of current attributes and pauses a moment
        original_created_at = new_obj.created_at
        original_updated_at = new_obj.updated_at
        sleep(1)
        # adds required attributes so the object can be saved; saves object
        new_obj.name = "test_name"
        new_obj.save()
        # tests that the object's updated_at has changed and is later
        self.assertNotEqual(original_updated_at, new_obj.updated_at)
        self.assertTrue(original_updated_at < new_obj.updated_at)
        # tests that only the object's updated_at datetime has changed
        self.assertEqual(original_created_at, new_obj.created_at)

    def test_init_method(self):
        """
        tests the __init__ method for instantiating new objects
        both new and from kwargs
        __init__ method calls on inherited BaseModel with super()
        """
        # creates new instance of Identity
        new_obj1 = Identity()
        # tests that the new object is of type Identity
        self.assertIs(type(new_obj1), Identity)
        # adds all attributes for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj1.name = "test_name"
        # attributes_dict sets up dictionary of attribute names and types
        attributes_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
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
        new_obj2 = Identity(**kwargs)
        # tests that the new object is of type Identity
        self.assertIs(type(new_obj2), Identity)
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
        this method is inherited from BaseModel, but should show Identityclass
        """
        # creates new instance of Identity and saves variables
        new_obj = Identity()
        obj_id = new_obj.id
        obj_dict = new_obj.__dict__
        # tests the string representation of object is formatted correctly
        self.assertEqual(str(new_obj),
                         "[Identity.{}] {}".format(obj_id, obj_dict))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """
        tests that the save() method inherited from BaseModel calls on
        storage.new() to add and commit the object to the database
        """
        # creates new instance of Identity
        new_obj = Identity()
        # adds name as required attribute for database
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves new instance and tests if storage method new is called
        new_obj.save()
        self.assertTrue(mock_storage.new.called)

    @mock.patch('models.storage')
    def test_delete_method(self, mock_storage):
        """
        tests that the delete() method inherited from BaseModel calls on
        storage.delete() to remove and commit the object from the database
        """
        # creates new instance of Identity
        new_obj = Identity()
        # adds name as required attribute for database
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves to database before attempting to delete
        new_obj.save()
        self.assertTrue(mock_storage.new.called)
        # deletes new instance and tests if storage method deleted is called
        new_obj.delete()
        self.assertTrue(mock_storage.delete.called)

    # functionality of save() and delete() methods are tested in unit tests
    # for DBStorage as the storage engine is doing the work to actually
    # save or delete the objects from the database
