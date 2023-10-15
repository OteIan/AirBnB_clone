#!/usr/bin/python3
"""
Test case module for City module
"""
import unittest
from models.city import City
import models.city as city_module


class TestCity(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.name = "City"
        self.city = City

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(city_module.__doc__)
        self.assertIsNotNone(City.__doc__)

    def test_attribute_type(self):
        """ """
        self.assertIsInstance(self.city().name, str)

    def test_str(self):
        """ """
        u = self.city()
        self.assertEqual(str(u), f"[{self.name}] ({u.id}) {u.__dict__}")

    def test_with_kwargs_only(self):
        """ """
        u = self.city(state_id="Founder", name="Great")
        result = []
        check_list = \
            ['state_id', 'name', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_only(self):
        """ """
        u = self.city(42, "remember", "yesterday", "city")
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_and_kwargs(self):
        """ """
        u = self.city(42, "remember", "yesterday", "city",
                      state_id="Jefferson", name="today")
        result = []
        check_list = \
            ['state_id', 'name', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)


if __name__ == "__main__":
    unittest.main()
