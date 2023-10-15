#!/usr/bin/python3
"""
Test case module for User module
"""
import unittest
from models.user import User
import models.user as user_module


class TestUser(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.user = User()

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(user_module.__doc__)
        self.assertIsNotNone(User.__doc__)

    def test_attributes_types(self):
        """ """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_init_with_no_args(self):
        """ """
        u = User()
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_init_with_kwargs_only(self):
        """ """
        u = User(email='myemail123@gmail.com', age=9)
        result = []
        check_list = \
            ['email', 'age', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_init_with_args_only(self):
        """ """
        u = User()
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_init_with_and_args_kwargs(self):
        """ """
        u = User(42, "new", "something", 0.02, email='myemail123@gmail.com',
                 password="empty", first_name="Ryan", last_name="Reynolds")
        result = []
        check_list = ['email', 'password', 'first_name', 'last_name', 'id',
                      'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_str(self):
        """ """
        u = User()
        self.assertEqual(str(u), f"[{User.__name__}] ({u.id}) {u.__dict__}")


if __name__ == "__main__":
    unittest.main()
