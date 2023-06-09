#!/usr/bin/python3
"""
Define a class of Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize all attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
