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
from MySQLdb import connect
from os import getenv
import pep8
from time import sleep
from unittest import TestCase
# establishes dictionary reference between class name and class itself
classes = {"Identity": Identity, "Profile": Profile, "Skills": Skills}
# sets variables from os environment variables set by user
ION_MYSQL_HOST = getenv('ION_MYSQL_HOST')
ION_MYSQL_USER = getenv('ION_MYSQL_USER')
ION_MYSQL_PWD = getenv('ION_MYSQL_PWD')
ION_MYSQL_DB = getenv('ION_MYSQL_DB')
ION_IS_TEST = getenv('ION_IS_TEST')


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

    def test_new_identity(self):
        """
        tests the storage.new() method adds and commits obj to database
        for an object from the Identity class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Identity
        new_obj = Identity()
        # tests that the new object is of type Identity
        self.assertIs(type(new_obj), Identity)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # save the object with BaseModel save method
        # save instance method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to identities table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # closes the connection
        cur.close()
        db.close()

    def test_new_profile(self):
        """
        tests the storage.new() method adds and commits obj to database
        for an object from the Profile class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Profile
        new_obj = Profile()
        # tests that the new object is of type Profile
        self.assertIs(type(new_obj), Profile)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        new_obj.email = "test@testing.com"
        # save the object with BaseModel save method
        # save instance method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to profiles table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # closes the connection
        cur.close()
        db.close()

    def test_new_skills(self):
        """
        tests the storage.new() method adds and commits obj to database
        for an object from the Skills class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Skills
        new_obj = Skills()
        # tests that the new object is of type Skills
        self.assertIs(type(new_obj), Skills)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # save the object with BaseModel save method
        # save instance method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to skills table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # closes the connection
        cur.close()
        db.close()

    def test_delete_identity(self):
        """
        tests the storage.delete() method removes and commits obj to database
        for an object from the Identity class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Identity
        new_obj = Identity()
        # tests that the new object is of type Identity
        self.assertIs(type(new_obj), Identity)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # save the object with BaseModel save method
        # save method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to identities table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # delete the object with BaseModel delete method
        # delete instance method calls storage.delete() and storage.save()
        new_obj.delete()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        objs_for_count3 = cur.fetchall()
        # tests that there is one less obj in identities table in db
        self.assertEqual(len(objs_for_count2) - 1, len(objs_for_count3))
        self.assertEqual(len(objs_for_count1), len(objs_for_count3))
        # closes the connection
        cur.close()
        db.close()

    def test_delete_profile(self):
        """
        tests the storage.delete() method removes and commits obj to database
        for an object from the Profile class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Profile
        new_obj = Profile()
        # tests that the new object is of type Profile
        self.assertIs(type(new_obj), Profile)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        new_obj.email = "test@testing.com"
        # save the object with BaseModel save method
        # save method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to profiles table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # delete the object with BaseModel delete method
        # delete instance method calls storage.delete() and storage.save()
        new_obj.delete()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        objs_for_count3 = cur.fetchall()
        # tests that there is one less obj in profiles table in db
        self.assertEqual(len(objs_for_count2) - 1, len(objs_for_count3))
        self.assertEqual(len(objs_for_count1), len(objs_for_count3))
        # closes the connection
        cur.close()
        db.close()

    def test_delete_skills(self):
        """
        tests the storage.delete() method removes and commits obj to database
        for an object from the Skills class
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        objs_for_count1 = cur.fetchall()
        # creates new instance of Skills
        new_obj = Skills()
        # tests that the new object is of type Skills
        self.assertIs(type(new_obj), Skills)
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # save the object with BaseModel save method
        # save method calls storage.new() and storage.save()
        new_obj.save()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        objs_for_count2 = cur.fetchall()
        # tests that there is one more obj saved to skills table in db
        self.assertEqual(len(objs_for_count1) + 1, len(objs_for_count2))
        # delete the object with BaseModel delete method
        # delete instance method calls storage.delete() and storage.save()
        new_obj.delete()
        # closes connection to database and restarts connection with MySQLdb
        cur.close()
        db.close()
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        objs_for_count3 = cur.fetchall()
        # tests that there is one less obj in skills table in db
        self.assertEqual(len(objs_for_count2) - 1, len(objs_for_count3))
        self.assertEqual(len(objs_for_count1), len(objs_for_count3))
        # closes the connection
        cur.close()
        db.close()

    def test_all_method(self):
        """
        tests all method retrieves all objects when class is not specified
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        identity_objs = cur.fetchall()
        cur.execute("""SELECT * FROM profiles""")
        profile_objs = cur.fetchall()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_count = len(identity_objs) + len(profile_objs) + len(skills_objs)
        # call storage.all() method
        all_objs = storage.all()
        # tests that all method returns same count of total objects
        self.assertEqual(total_count, len(all_objs.keys()))
        # tests that all method returns dictionary
        self.assertIsInstance(all_objs, dict)

    def test_all_identities_count(self):
        """
        tests all method retrieves all objects when class is Identity
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        identity_objs = cur.fetchall()
        cur.execute("""SELECT * FROM profiles""")
        profile_objs = cur.fetchall()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_count = len(identity_objs) + len(profile_objs) + len(skills_objs)
        total_identity_count = len(identity_objs)
        # call storage.all() method, both with and without class specified
        all_objs = storage.all()
        count1 = len(all_objs.keys())
        all_identity_objs = storage.all(Identity)
        identity_count1 = len(all_identity_objs.keys())
        # tests that counts from all method match current database
        self.assertEqual(total_count, count1)
        self.assertEqual(total_identity_count, identity_count1)
        # creates new Identity obj to test with
        new_obj = Identity()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method
        all_objs = storage.all()
        count2 = len(all_objs.keys())
        all_identity_objs = storage.all(Identity)
        identity_count2 = len(all_identity_objs.keys())
        # tests that counts increased by 1
        self.assertEqual(count1 + 1, count2)
        self.assertEqual(identity_count1 + 1, identity_count2)
        # deletes new object from the database
        new_obj.delete()
        # re-call storage.all() method
        all_objs = storage.all()
        count3 = len(all_objs.keys())
        all_identity_objs = storage.all(Identity)
        identity_count3 = len(all_identity_objs.keys())
        # tests that count decreased by 1
        self.assertEqual(count2 - 1, count3)
        self.assertEqual(count1, count3)
        self.assertEqual(identity_count2 - 1, identity_count3)
        self.assertEqual(identity_count1, identity_count3)

    def test_all_identities_dict(self):
        """
        tests return of all method when class is Identity
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        identity_objs = cur.fetchall()
        total_identity_count = len(identity_objs)
        # call storage.all() method
        all_identity_objs = storage.all(Identity)
        identity_count1 = len(all_identity_objs.keys())
        # tests that all method returns same count of Identity objects
        self.assertEqual(total_identity_count, identity_count1)
        # tests that all method returns dictionary
        self.assertIsInstance(all_identity_objs, dict)
        # creates new Identity obj to test with
        new_obj = Identity()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method and test that count increased by 1
        all_identity_objs = storage.all(Identity)
        identity_count2 = len(all_identity_objs.keys())
        self.assertEqual(identity_count1 + 1, identity_count2)
        # tests that newly created obj is in dictionary with correct key
        self.assertIsInstance(storage.all(), dict)
        dict_key = "{}.{}".format("Identity", new_obj.id)
        self.assertIn(dict_key, storage.all())
        # get obj attributes from stroage.all() dictionary using obj id
        # test that retrieved attributes match expected values
        obj_class = storage.all().get("Identity.{}".
                                      format(new_obj.id)).__class__.__name__
        self.assertEqual("Identity", obj_class)
        obj_name = storage.all().get("Identity.{}".
                                     format(new_obj.id)).name
        self.assertEqual("test_name", obj_name)
        # delete new object from the database
        new_obj.delete()
        # re-call storage.all() method and test that count decreased by 1
        all_identity_objs = storage.all(Identity)
        identity_count3 = len(all_identity_objs.keys())
        self.assertEqual(identity_count2 - 1, identity_count3)
        self.assertEqual(identity_count1, identity_count3)
        # tests that new object is no longer in return dictionary
        self.assertNotIn(dict_key, storage.all())

    def test_all_profiles_count(self):
        """
        tests all method retrieves all objects when class is Profile
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        identity_objs = cur.fetchall()
        cur.execute("""SELECT * FROM profiles""")
        profile_objs = cur.fetchall()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_count = len(identity_objs) + len(profile_objs) + len(skills_objs)
        total_profile_count = len(profile_objs)
        # call storage.all() method, both with and without class specified
        all_objs = storage.all()
        count1 = len(all_objs.keys())
        all_profile_objs = storage.all(Profile)
        profile_count1 = len(all_profile_objs.keys())
        # tests that counts from all method match current database
        self.assertEqual(total_count, count1)
        self.assertEqual(total_profile_count, profile_count1)
        # creates new Profile obj to test with
        new_obj = Profile()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        new_obj.email = "test@testing.com"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method
        all_objs = storage.all()
        count2 = len(all_objs.keys())
        all_profile_objs = storage.all(Profile)
        profile_count2 = len(all_profile_objs.keys())
        # tests that counts increased by 1
        self.assertEqual(count1 + 1, count2)
        self.assertEqual(profile_count1 + 1, profile_count2)
        # deletes new object from the database
        new_obj.delete()
        # re-call storage.all() method
        all_objs = storage.all()
        count3 = len(all_objs.keys())
        all_profile_objs = storage.all(Profile)
        profile_count3 = len(all_profile_objs.keys())
        # tests that count decreased by 1
        self.assertEqual(count2 - 1, count3)
        self.assertEqual(count1, count3)
        self.assertEqual(profile_count2 - 1, profile_count3)
        self.assertEqual(profile_count1, profile_count3)

    def test_all_profiles_dict(self):
        """
        tests return of all method when class is Profile
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM profiles""")
        profile_objs = cur.fetchall()
        total_profile_count = len(profile_objs)
        # call storage.all() method
        all_profile_objs = storage.all(Profile)
        profile_count1 = len(all_profile_objs.keys())
        # tests that all method returns same count of Identity objects
        self.assertEqual(total_profile_count, profile_count1)
        # tests that all method returns dictionary
        self.assertIsInstance(all_profile_objs, dict)
        # creates new Profile obj to test with
        new_obj = Profile()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        new_obj.email = "test@testing.com"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method and test that count increased by 1
        all_profile_objs = storage.all(Profile)
        profile_count2 = len(all_profile_objs.keys())
        self.assertEqual(profile_count1 + 1, profile_count2)
        # tests that newly created obj is in dictionary with correct key
        self.assertIsInstance(storage.all(), dict)
        dict_key = "{}.{}".format("Profile", new_obj.id)
        self.assertIn(dict_key, storage.all())
        # get obj attributes from stroage.all() dictionary using obj id
        # test that retrieved attributes match expected values
        obj_class = storage.all().get("Profile.{}".
                                      format(new_obj.id)).__class__.__name__
        self.assertEqual("Profile", obj_class)
        obj_name = storage.all().get("Profile.{}".
                                     format(new_obj.id)).name
        self.assertEqual("test_name", obj_name)
        obj_email = storage.all().get("Profile.{}".
                                      format(new_obj.id)).email
        self.assertEqual("test@testing.com", obj_email)
        # delete new object from the database
        new_obj.delete()
        # re-call storage.all() method and test that count decreased by 1
        all_profile_objs = storage.all(Profile)
        profile_count3 = len(all_profile_objs.keys())
        self.assertEqual(profile_count2 - 1, profile_count3)
        self.assertEqual(profile_count1, profile_count3)
        # tests that new object is no longer in return dictionary
        self.assertNotIn(dict_key, storage.all())

    def test_all_skills_count(self):
        """
        tests all method retrieves all objects when class is Skills
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM identities""")
        identity_objs = cur.fetchall()
        cur.execute("""SELECT * FROM profiles""")
        profile_objs = cur.fetchall()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_count = len(identity_objs) + len(profile_objs) + len(skills_objs)
        total_skills_count = len(skills_objs)
        # call storage.all() method, both with and without class specified
        all_objs = storage.all()
        count1 = len(all_objs.keys())
        all_skills_objs = storage.all(Skills)
        skills_count1 = len(all_skills_objs.keys())
        # tests that counts from all method match current database
        self.assertEqual(total_count, count1)
        self.assertEqual(total_skills_count, skills_count1)
        # creates new Skills obj to test with
        new_obj = Skills()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method
        all_objs = storage.all()
        count2 = len(all_objs.keys())
        all_skills_objs = storage.all(Skills)
        skills_count2 = len(all_skills_objs.keys())
        # tests that counts increased by 1
        self.assertEqual(count1 + 1, count2)
        self.assertEqual(skills_count1 + 1, skills_count2)
        # deletes new object from the database
        new_obj.delete()
        # re-call storage.all() method
        all_objs = storage.all()
        count3 = len(all_objs.keys())
        all_skills_objs = storage.all(Skills)
        skills_count3 = len(all_skills_objs.keys())
        # tests that count decreased by 1
        self.assertEqual(count2 - 1, count3)
        self.assertEqual(count1, count3)
        self.assertEqual(skills_count2 - 1, skills_count3)
        self.assertEqual(skills_count1, skills_count3)

    def test_all_skills_dict(self):
        """
        tests return of all method when class is Skills
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_skills_count = len(skills_objs)
        # call storage.all() method
        all_skills_objs = storage.all(Skills)
        skills_count1 = len(all_skills_objs.keys())
        # tests that all method returns same count of Skills objects
        self.assertEqual(total_skills_count, skills_count1)
        # tests that all method returns dictionary
        self.assertIsInstance(all_skills_objs, dict)
        # creates new Skills obj to test with
        new_obj = Skills()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj.name = "test_name"
        # saves new object to the database
        new_obj.save()
        # re-call storage.all() method and test that count increased by 1
        all_skills_objs = storage.all(Skills)
        skills_count2 = len(all_skills_objs.keys())
        self.assertEqual(skills_count1 + 1, skills_count2)
        # tests that newly created obj is in dictionary with correct key
        self.assertIsInstance(storage.all(), dict)
        dict_key = "{}.{}".format("Skills", new_obj.id)
        self.assertIn(dict_key, storage.all())
        # get obj attributes from stroage.all() dictionary using obj id
        # test that retrieved attributes match expected values
        obj_class = storage.all().get("Skills.{}".
                                      format(new_obj.id)).__class__.__name__
        self.assertEqual("Skills", obj_class)
        obj_name = storage.all().get("Skills.{}".
                                     format(new_obj.id)).name
        self.assertEqual("test_name", obj_name)
        # delete new object from the database
        new_obj.delete()
        # re-call storage.all() method and test that count decreased by 1
        all_skills_objs = storage.all(Skills)
        skills_count3 = len(all_skills_objs.keys())
        self.assertEqual(skills_count2 - 1, skills_count3)
        self.assertEqual(skills_count1, skills_count3)
        # tests that new object is no longer in return dictionary
        self.assertNotIn(dict_key, storage.all())

    def test_reload(self):
        """
        tests that the reload function creates a new session
        linked only to current database tables
        """
        # connect to MySQL database through MySQLdb and get initial count
        db = connect(host=ION_MYSQL_HOST,
                     user=ION_MYSQL_USER,
                     passwd=ION_MYSQL_PWD,
                     db=ION_MYSQL_DB)
        cur = db.cursor()
        cur.execute("""SELECT * FROM skills""")
        skills_objs = cur.fetchall()
        total_skills_count = len(skills_objs)
        # call storage.all() method
        all_skills_objs = storage.all(Skills)
        skills_count1 = len(all_skills_objs.keys())
        # tests that all method returns same count of Skills objects
        self.assertEqual(total_skills_count, skills_count1)
        # creates new Skills obj to test with; obj is saved
        new_obj1 = Skills()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj1.name = "test_name1"
        # saves new object to the database
        new_obj1.save()
        # creates new Skills obj to test with; obj is not saved
        new_obj2 = Skills()
        # adds all attributes required for testing
        # (id should be set by primary key)
        # (created_at, updated_at should be set by datetime)
        new_obj2.name = "test_name2"
        # call reload method to reconnect session to current database
        storage.reload()
        # re-call storage.all() method and test that count increased by only 1
        all_skills_objs = storage.all(Skills)
        skills_count2 = len(all_skills_objs.keys())
        self.assertEqual(skills_count1 + 1, skills_count2)
        # tests that newly created saved obj is in dictionary with correct key
        dict_key = "{}.{}".format("Skills", new_obj1.id)
        self.assertIn(dict_key, storage.all())
        # tests that newly created unsaved obj is not in dictionary
        dict_key = "{}.{}".format("Skills", new_obj2.id)
        self.assertNotIn(dict_key, storage.all())

    def test_storage_get_method(self):
        """
        test get method to retrieve specific object
        """
        for cls in ["Identity", "Profile", "Skills"]:
            with self.subTest(cls=cls):
                # tests get method when id does not exist
                self.assertIs(storage.get(cls, -89), None)
                # creates new obj to test with and saves to database
                new_obj = classes[cls]()
                new_obj.name = "test_name"
                if cls == "Profile":
                    new_obj.email = "test@testing.com"
                new_obj.save()
                # tests get method with valid class name and id
                got_obj = storage.get(cls, new_obj.id)
                self.assertIs(got_obj.__class__.__name__, cls)
                self.assertEqual(got_obj.id, new_obj.id)
