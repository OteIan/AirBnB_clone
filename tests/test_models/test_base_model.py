import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from os.path import isfile


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_created_at_and_updated_at_on_init(self):
        new_model = BaseModel()
        created_base = self.base_model.created_at
        updated_base = self.base_model.updated_at
        self.assertEqual(created_base, updated_base)
        self.assertNotEqual(created_base, new_model.created_at)
        self.assertNotEqual(updated_base, new_model.updated_at)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_json_serilization(self):
        self.base_model.save()
        self.assertTrue(isfile("file.json"))

    def test_from_json_deserilization(self):
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertTrue(obj)


if __name__ == '__main__':
    unittest.main()
