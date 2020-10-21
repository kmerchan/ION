#!/usr/bin/python3
"""
this module defines unit tests for Profile
testing functionality and documentation
"""
from datetime import datetime
from inspect import getmembers, isfunction
from models.base_model import BaseModel
from models.profile import Profile, __doc__ as profile_doc
import pep8
from unittest import TestCase


class Test_Profile_Docs(TestCase):
    """
    defines tests to check documentation and style
    for Profile module, class, and methods
    """

    @classmethod
    def setUpClass(self):
        """
        uses inspect to get all methods to test for docstrings
        saves as profile_methods attribute to call later
        """
        self.profile_methods = getmembers(Profile, isfunction)

    def test_pep8_style(self):
        """
        tests that models/profile.py
        and tests/test_models/test_profile.py
        follows pep8 style guidelines
        """
        for path in ['models/profile.py',
                     'tests/test_models/test_profile.py']:
            # tests each path as a subTest for 0 pep8 errors
            with self.subTest(path=path):
                errors = pep8.Checker(path).check_all()
                self.assertEqual(errors, 0,
                                 "pep8 is returning errors for {}".
                                 format(path))

    def test_module_docstring(self):
        """
        tests that models.profile module contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(profile_doc, None,
                         "profile module is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(profile_doc) > 1,
                        "profile module is missing docstring")

    def test_class_docstring(self):
        """
        tests that the Profile class contains docstring
        """
        # first tests if docstring is not None
        self.assertIsNot(Profile.__doc__, None,
                         "Profile class is missing docstring")
        # then tests if there is at least 1 docstring
        self.assertTrue(len(Profile.__doc__) > 1,
                        "Profile class is missing docstring")

    def test_method_docstrings(self):
        """
        tests that all methods in Profile have docstrings
        """
        for method in self.profile_methods:
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


class Test_Profile(TestCase):
    """
    defines tests to check functionality
    of Profile class attributes and methods
    """

    def test_class_and_subclass(self):
        """
        tests that instances are of Profile class
        and are a subclass of BaseModel class
        """
        new_obj = Profile()
        # tests that the new instance is of type Profile
        self.assertIs(type(new_obj), Profile)
        # tests that the new instance is a subclass of BaseModel
        self.assertIsInstance(new_obj, BaseModel)

    def test_attribute_types(self):
        """
        tests the class attributes exist and are of correct type
        also tests instantiation of new object
        """
        # creates new instance of Profile
        new_obj = Profile()
        # adds name and email as required attribute for database
        # adds optional attributes for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        new_obj.email = "test@testing.com"
        new_obj.password = "test_password_123"
        new_obj.company_school_name = "123"
        new_obj.about_me = "This is for testing purposes"
        new_obj.linkedin = "https://www.linkedin.com/in/test"
        new_obj.social_media = "Social media links would go here"
        # attributes_dict sets up dictionary of attribute names and types
        attributes_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "email": str,
            "password": str,
            "company_school_name": str,
            "about_me": str,
            "linkedin": str,
            "social_media": str
        }
        # loops through attributes_dict as subTests to check each attribute
        for attr, attr_type in attributes_dict.items():
            with self.subTest(attr=attr, attr_type=attr_type):
                # tests the expected attribute is in the instance's dict
                self.assertIn(attr, new_obj.__dict__)
                # tests the attribute is the expected type
                self.assertIs(type(new_obj.__dict__[attr]), attr_type)

    def test_init_method(self):
        """
        tests the __init__ method for instantiating new objects
        both new and from kwargs
        __init__ method calls on inherited BaseModel with super()
        """
        # creates new instance of Profile
        new_obj1 = Profile()
        # tests that the new object is of type Profile
        self.assertIs(type(new_obj1), Profile)
        # adds all attributes for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj1.name = "test_name"
        new_obj1.email = "test@testing.com"
        new_obj1.password = "test_password_123"
        new_obj1.company_school_name = "123"
        new_obj1.about_me = "This is for testing purposes"
        new_obj1.linkedin = "https://www.linkedin.com/in/test"
        new_obj1.social_media = "Social media links would go here"
        # attributes_dict sets up dictionary of attribute names and types
        attributes_dict = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "email": str,
            "password": str,
            "company_school_name": str,
            "about_me": str,
            "linkedin": str,
            "social_media": str
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
        new_obj2 = Profile(**kwargs)
        # tests that the new object is of type Profile
        self.assertIs(type(new_obj2), Profile)
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
        this method is inherited from BaseModel, but should show Profile class
        """
        # creates new instance of Profile and saves variables
        new_obj = Profile()
        obj_id = new_obj.id
        obj_dict = new_obj.__dict__
        # tests the string representation of object is formatted correctly
        self.assertEqual(str(new_obj),
                         "[Profile.{}] {}".format(obj_id, obj_dict))
