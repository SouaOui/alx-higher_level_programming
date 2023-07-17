#!/usr/bin/python3
"""Create a SubClass from Rectangle Class (SubClass of Base)"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Write the class Rectangle that inherits
    from Rectanlge(SubClass of Base)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize attribute for square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method for width"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """print the information of a class in good way"""
        new_string = ""
        new_string += "[square] "
        new_string += "({}) {}/{} ".format(self.id, self.x, self.y)
        new_string += "- {}".format(self.width)
        return new_string
