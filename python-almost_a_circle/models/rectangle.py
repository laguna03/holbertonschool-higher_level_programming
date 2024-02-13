#!/usr/usr/bin/python3
""" Rectangle class that inherits from Base"""


from models.base import Base

class Rectangle:
    """ Rectangle class that inherits from Base"""



    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the Rectangle class """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is not None:
            self.id = id
        else:
            """ Increment the number of objects"""

            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def width(self):
        """Getter for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

        @property
        def height(self):
            """Getter for height"""

            return self.__height

        @height.setter
        def height(self, value):
            """setter for height"""
            if not isinstance(value, int):
                raise TypeError("Height must be an int")
            elif value < 0:
                raise ValueError("Height must but => 0")
            else:
                self.__height = value

        @property
        def x(self):
            """Getter for x"""

            return self.__x

        @x.setter
        def x(self, value):
            """setter for x"""
            if not isinstance(value, int):
                raise TypeError("x must be an int")
            elif value < 0:
                raise ValueError("x must be => 0")
            else:
                self.__x = value

        @property
        def y(self):
            """Getter for y"""

            return self.__y

        @y.setter
        def y(self, value):
            """setter for y"""
            if not isinstance(value, int):
                raise TypeError("y must be an int")
            elif value < 0:
                raise ValueError("y must be => 0")
            else:
                self.__y = value
