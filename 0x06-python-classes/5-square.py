#!/usr/bin/python3
"""define a class that calculate a square of number"""


class Square:
    """Represent a operation square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculate the area"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print using # symbol"""
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
