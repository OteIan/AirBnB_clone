#!/usr/bin/python3
"""
Test case module for Review module
"""
import unittest
from models.review import Review
import models.review as review_module


class Testreview(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.name = "Review"
        self.review = Review

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(review_module.__doc__)
        self.assertIsNotNone(Review.__doc__)

    def test_attribute_type(self):
        """ """
        self.assertIsInstance(self.review().place_id, str)
        self.assertIsInstance(self.review().user_id, str)
        self.assertIsInstance(self.review().text, str)       

    def test_str(self):
        """ """
        u = self.review()
        self.assertEqual(str(u), f"[{self.name}] ({u.id}) {u.__dict__}")

    def test_with_kwargs_only(self):
        """ """
        u = self.review(place_id="current", user_id="now", text="Founder")
        result = []
        check_list = ['place_id', "user_id", "text", 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_only(self):
        """ """
        u = self.review(42, "remember", "yesterday", "review")
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_and_kwargs(self):
        """ """
        u = self.review(42, "remember", "yesterday", "review",
                         place="Jefferson", user_id="now", text="today")
        result = []
        check_list = ['place', 'user_id', "text", 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)


if __name__ == "__main__":
    unittest.main()
