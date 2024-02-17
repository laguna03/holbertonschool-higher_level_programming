#!/usr/bin/python3
""" Rectangle class that inherits from Base"""

from models.base import Base


class Rectangle:
    """ Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the Rectangle class """
        super().__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is None:
            self.id = Base().id
        else:
            self.id = id
            Base().id = id

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        return 2 * (self.__width + self.__height)
#!/usr/bin/python3
"""Recntagle class that inherits from Base"""

import sys
from models.base import Base


class Rectangle(Base):
    """Recntagle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Returns the display of the Rectangle"""
        for y in range(self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end='')
            print()
        # """Returns the display of the Rectangle"""
        # for i in range(0, self.__height):
        #     for j in range(0, self.__width):
        #         print("#", end='')
        #     print()

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        p = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        p1 = f" - {self.__width}/{self.__height}"
        return p + p1

    def check_arguments(self, *args, **kwargs):
        """
        Checks the arguments
        """
        if args and kwargs or args:
            return 1
        if kwargs and args is None:
            return 2

    def update(self, *args, **kwargs):
        """Updates the rectangle with the given args"""
        # if args and kwargs or args is not None:
        if self.check_arguments(*args, **kwargs) == 1:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """
        Returns a dictionary representation
        """
        collage = {
            "x": {self.x},
            "y": {self.y},
            "id": {self.id},
            "width": {self.width},
            "height": {self.height}
        }
        return collage
