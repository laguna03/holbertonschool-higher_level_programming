#!/usr/bin/python3
"""
Module Rectangle
"""
__height = None
__width = None

class Rectangle:
    """Define rectangle class"""

    def __init__(self, width=0, height=0):
        """init function"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = width
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
