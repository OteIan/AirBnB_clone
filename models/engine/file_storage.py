import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
"""
This module saves contents of a class onto a file
"""


class FileStorage:
    """
    This class handles saving and loading instances of classes
      to/from a JSON file.
    """
    __file_path = "file.json"
    """
    The path to the JSON file where instances are stored.
    """
    __objects = {}
    """
    A dictionary to store instances where keys are in the format:
        "<class name>.<instance id>".
    """
    def all(self):
        """
        Retrieve all instances currently stored in the FileStorage.
        Returns:
            dict: A dictionary containing all stored instances.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new instance to the FileStorage.
        Args:
            obj: The instance to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize and save all instances to the JSON file.
        """
        objects_dict = \
            {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """
        Deserialize and load instances from the JSON file into the FileStorage.
        """
        try:
            with open(self.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
