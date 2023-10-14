#!/usr/bin/python3
"""
Test case module for State module
"""
import unittest
from models.state import State
import models.state as state_module


class Teststate(unittest.TestCase):
    """ """
    def setUp(self):
        """ """
        self.name = "State"
        self.state = State

    def tearDown(self):
        """ """
        pass

    def test_docstrings(self):
        """ """
        self.assertIsNotNone(state_module.__doc__)
        self.assertIsNotNone(State.__doc__)

    def test_attribute_type(self):
        """ """
        self.assertIsInstance(self.state().name, str)

    def test_str(self):
        """ """
        u = self.state()
        self.assertEqual(str(u), f"[{self.name}] ({u.id}) {u.__dict__}")

    def test_with_kwargs_only(self):
        """ """
        u = self.state(name="Founder")
        result = []
        check_list = ['name', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_only(self):
        """ """
        u = self.state(42, "remember", "yesterday", "state")
        result = []
        check_list = ['id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)

    def test_with_args_and_kwargs(self):
        """ """
        u = self.state(42, "remember", "yesterday", "state",
                         name="Jefferson", time="today")
        result = []
        check_list = ['name', 'time', 'id', 'created_at', 'updated_at', '__class__']
        for key in u.to_dict():
            result.append(key)
        self.assertListEqual(result, check_list)


if __name__ == "__main__":
    unittest.main()
