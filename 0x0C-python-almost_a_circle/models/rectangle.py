#!/usr/bin/python3
"""Create a SubClass from Base Class"""


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


class Rectangle(Base):
    """Write the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize fields for the Rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the area of Rectangle using '#' """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(' ', end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update Public method assign an argument to each attribute"""
        attributes_name = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes_name[i], arg)
        for key, value in kwargs.items():
            if key in attributes_name:
                setattr(self, key, value)

    def __str__(self):
        """print the information of a class in good way"""
        new_string = ""
        new_string += "[Rectangle] "
        new_string += "({}) {}/{} ".format(self.id, self.x, self.y)
        new_string += "- {}/{}".format(self.__width, self.__height)
        return new_string
