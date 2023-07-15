#!/usr/bin/python3
"""define a class that calculate a square of number"""


class Square:
    """Declare a Square class"""
    def __init__(self, size=0, position=(0,0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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
    @property
    def position(self):
        """retrieve the position"""
        return self.__position
    
    @position.setter
    def position(position, value):
        if not isinstance(position, tuple) and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            
            
    
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

