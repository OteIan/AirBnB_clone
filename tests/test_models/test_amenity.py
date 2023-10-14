#!/usr/bin/python3
"""
Test case module for Amenity module
"""
import unittest
from models.amenity import Amenity
import models.amenity as amenity_module


class TestAmenity(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.name = "Amenity"
        self.amenity = Amenity

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(amenity_module.__doc__)
        self.assertIsNotNone(Amenity.__doc__)

    def test_attribute_type(self):
        """ """
        self.assertIsInstance(self.amenity().name, str)

    def test_str(self):
        """ """
        u = self.amenity()
        self.assertEqual(str(u), f"[{self.name}] ({u.id}) {u.__dict__}")

    def test_with_kwargs_only(self):
        """ """
        u = self.amenity(day="Founder")
        result = []
        check_list = ['day', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_only(self):
        """ """
        u = self.amenity(42, "remember", "yesterday", "Amenity")
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_and_kwargs(self):
        """ """
        u = self.amenity(42, "remember", "yesterday", "Amenity",
                         name="Jefferson", time="today")
        result = []
        check_list = ['name', 'time', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)



if __name__ == "__main__":
    unittest.main()
