#!/usr/bin/python3
"""Create a new class Base"""
import json


class Base:
    """Create a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method for class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return The Json Representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write Json Representation of list_objs to a file"""
        new_list = []
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding='utf-8') as file:
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            mystring = Base.to_json_string(new_list)
            file.write(mystring)

    @staticmethod
    def from_json_string(json_string):
        """ load the representation for the object with string"""
        if json_string is None:
            return []
        return json.loads(json_string)
