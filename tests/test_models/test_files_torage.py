#!/usr/bin/python3
"""
Test cases for filestorage
"""
import unittest
import os
import json
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

    def test_all_method_returns_dictionary(self):
        """
        Test if the all method returns a dictionary.
        """
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method_adds_to_objects(self):
        """
        Test if the new method adds an object to the __objects dictionary.
        """
        user = User()
        self.file_storage.new(user)
        self.assertIn('User.{}'.format(user.id), self.file_storage.all())

    def test_save_method_creates_json_file(self):
        """
        Test if the save method creates a JSON file.
        """
        self.file_storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        os.remove(FileStorage._FileStorage__file_path)

    def test_reload_method_loads_objects_from_json(self):
        """
        Test if the reload method loads objects
          from a JSON file into __objects.
        """
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertIn('User.{}'.format(user.id), all_objects)
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
