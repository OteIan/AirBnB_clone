#!/usr/bin/python3
"""
Test cases for filestorage
"""
import unittest
import os
import json
import models.engine.file_storage as file_storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test case class for the FileStorage class.

    This class contains unit tests
      for various methods of the FileStorage class.
    """
    def setUp(self):
        """
        Set up a new instance of FileStorage before each test.
        """
        self.file_storage = FileStorage()
        self.file_storage.reload()

    def tearDown(self):
        """
        Remove the JSON file after the test
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_docsrings(self):
        """Test for module, class and function docstrings"""
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        
    def test_initial_list_is_empty(self):
        """"""
        self.assertEqual(len(storage.all()), 0)

    def test_all_method_returns_dictionary(self):
        """
        Test if the all method returns a dictionary.
        """
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method_adds_to_objects(self):
        """
        Test if the new method adds an object to the __objects dictionary.
        """
        user = User()
        storage.new(user)
        self.assertIn(f'User.{user.id}', storage.all())

    def test_save_method_creates_json_file(self):
        """
        Test if the save method creates a JSON file.
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method_loads_objects_from_json(self):
        """
        Test if the reload method loads objects
          from a JSON file into __objects.
        """
        new = BaseModel()
        storage.save()
        storage.reload()
        loaded = storage.all().get(f"{BaseModel.__name__}.{new.id}")
        self.assertIsNotNone(loaded)
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])


if __name__ == '__main__':
    unittest.main()
