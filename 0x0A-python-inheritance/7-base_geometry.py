#!/usr/bin/python3
"""define a class named BaseGeometry as a baseclass."""


class BaseGeometry:
    """Represent a BaseGeometry operation"""
    pass

    def area(self):
        """define the area of BaseGeometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
