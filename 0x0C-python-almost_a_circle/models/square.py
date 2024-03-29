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
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """print the information of a class in good way"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """public method to update attributes"""
        attributes_name = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes_name[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes_name:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the Represenation Dict of the square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
