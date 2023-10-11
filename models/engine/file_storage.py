import json

class FileStorage:
    __file_path = ""
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        with open(FileStorage.__file_path, "r") as file:
            return json.load(file)