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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
