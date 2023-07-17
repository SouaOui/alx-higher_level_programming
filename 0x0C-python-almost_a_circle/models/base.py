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
        list_new = []
        if list_dictionaries is None:
            return list_new
        return json.dumps(list_dictionaries)
