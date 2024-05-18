#!/usr/bin/python3

# models/engine/file_storage.py

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                serialized_objects = json.load(f)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals()[class_name]
                    self.__objects[key] = obj_class(**obj_dict)