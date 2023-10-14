#!/usr/bin/python3
"""
Test cases for basemodel
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from os.path import isfile


class TestBaseModel(unittest.TestCase):
    """
    Test case class for the BaseModel class.

    This class contains unit tests for various methods and properties
    of the BaseModel class.
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel before each test.
        """
        self.base_model = BaseModel()

    def test_id_generation(self):
        """
        Test if BaseModel generates a non-empty string ID.
        """
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at(self):
        """
        Test if created_at and updated_at attributes are instances of datetime.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_created_at_and_updated_at_on_init(self):
        """
        Test if created_at and updated_at are equal on initialization
        and different after creating a new instance of BaseModel.
        """
        new_model = BaseModel()
        created_base = self.base_model.created_at
        updated_base = self.base_model.updated_at
        self.assertEqual(created_base, updated_base)
        self.assertNotEqual(created_base, new_model.created_at)
        self.assertNotEqual(updated_base, new_model.updated_at)

    def test_save_updates_updated_at(self):
        """
        Test if the save method updates the updated_at attribute.
        """
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        """
        Test if the to_dict method returns a dictionary with the correct keys.
        """
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_json_serialization(self):
        """
        Test if the save method creates a JSON file.
        """
        self.base_model.save()
        self.assertTrue(isfile("file.json"))

    def test_from_json_deserialization(self):
        """
        Test if objects can be deserialized from the JSON file.
        """
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertTrue(obj)


if __name__ == '__main__':
    unittest.main()
