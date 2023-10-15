#!/usr/bin/python3
"""
Test case module for Place module
"""
import unittest
from models.place import Place
import models.place as place_module


class Testplace(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.name = "Place"
        self.place = Place

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(place_module.__doc__)
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_type(self):
        """ """
        self.assertIsInstance(self.place().city_id, str)
        self.assertIsInstance(self.place().user_id, str)
        self.assertIsInstance(self.place().name, str)
        self.assertIsInstance(self.place().description, str)
        self.assertIsInstance(self.place().number_rooms, int)
        self.assertIsInstance(self.place().number_bathrooms, int)
        self.assertIsInstance(self.place().max_guest, int)
        self.assertIsInstance(self.place().price_by_night, int)
        self.assertIsInstance(self.place().latitude, float)
        self.assertIsInstance(self.place().amenity_ids, str)

    def test_str(self):
        """ """
        u = self.place()
        self.assertEqual(str(u), f"[{self.name}] ({u.id}) {u.__dict__}")

    def test_with_kwargs_only(self):
        """ """
        u = self.place(day="Founder")
        result = []
        check_list = ['day', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_only(self):
        """ """
        u = self.place(42, "remember", "yesterday", "place")
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_and_kwargs(self):
        """ """
        u = self.place(42, "remember", "yesterday", "place",
                       name="Jefferson", time="today")
        result = []
        check_list = \
            ['name', 'time', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)


if __name__ == "__main__":
    unittest.main()
