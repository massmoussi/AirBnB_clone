#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    """Class to handle serialization and deserialization of objects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "User":
                        obj = User(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
