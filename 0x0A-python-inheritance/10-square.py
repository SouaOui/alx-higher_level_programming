#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, size):
        """Intialize a new Rectangle.

        Args:
            size (int): The height of the new Rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
