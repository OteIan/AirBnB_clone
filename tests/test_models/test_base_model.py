#!/usr/bin/python3
"""Test cases for basemodel
"""
import unittest
import models.base_model as base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from models import storage
from os.path import isfile
import os
import time


class TestBaseModel(unittest.TestCase):
    """Test case class for the BaseModel class.

    This class contains unit tests for various methods and properties
    of the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.base_model = BaseModel

    def setUp(self):
        """Set up a new instance of BaseModel before each test.
        """
        pass

    def tearDown(self):
        """ """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes(self):
        """Tests if the rewuired attributes are present"""
        self.assertTrue(hasattr(self.base_model(), "id"))
        self.assertTrue(hasattr(self.base_model(), "created_at"))
        self.assertTrue(hasattr(self.base_model(), "updated_at"))

    def test_docstrings(self):
        """Test for module, class and function docstring"""
        self.assertIsNotNone(base_model.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_default(self):
        """"""
        i = self.base_model()
        self.assertEqual(type(i), self.base_model)

    # Test cases for 'kwargs'
    def test_kwargs(self):
        """"""
        i = self.base_model()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.base_model()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = self.base_model(**copy)

    def test_kwargs_none(self):
        """ """
        i = {None: None}
        with self.assertRaises(TypeError):
            new = self.base_model(**i)

    def test_id_generation(self):
        """Test if BaseModel generates a non-empty string ID.
        """
        self.assertIsNotNone(self.base_model().id)
        self.assertIsInstance(self.base_model().id, str)

    def test_created_at_and_updated_at(self):
        """
        Test if created_at and updated_at attributes are instances of datetime
        """
        self.assertIsInstance(self.base_model().created_at, datetime)
        self.assertIsInstance(self.base_model().updated_at, datetime)

    def test_created_at_and_updated_at_on_init(self):
        """Test if created_at and updated_at are equal on initialization
        and different after creating a new instance of BaseModel.
        """
        new_model = BaseModel()
        time.sleep(0.02)
        created_base = self.base_model().created_at
        updated_base = self.base_model().updated_at
        created_new = new_model.created_at
        updated_new = new_model.updated_at

        self.assertEqual(created_base, updated_base)
        self.assertNotEqual(created_base, created_new)
        self.assertNotEqual(updated_base, updated_new)

    def test_save_updates_updated_at(self):
        """Test if the save method updates the updated_at attribute.
        """
        base_model = self.base_model()
        time.sleep(0.02)
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test if the to_dict method returns a dictionary with the correct keys
        """
        obj_dict = self.base_model().to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_str(self):
        """ """
        i = self.base_model()
        self.assertEqual(str(i), f'[{self.name}] ({i.id}) {i.__dict__}')


if __name__ == '__main__':
    unittest.main()
