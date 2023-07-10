#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, size):
        """Intialize a new square.

        Args:
            size (int): The size of the new Rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implement area method for square"""
        return self.__size ** 2
