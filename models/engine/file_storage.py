#!/usr/bin/python3
"""Defines FileStorage class."""
import json


class FileStorage:
    """
    Class FileStorage
    Represent an abstracted storage test_engine.

    It serializes instances to a JSON file and deserializes
    JSON file to instances.
    Attributes:
        __file_path (str): Name of the file to save objects to.
        __objects (dict): Dictionary of instantiated objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with the  key <obj_class_name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path."""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file does not
        exist, no exception should be raised)
        """

        # add all import below to avoid circular dependencies
        # eg. models imports file_storage, if file_storage imports models,
        # it becomes circular
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass
