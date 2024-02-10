#!/usr/bin/python3
"""Module for BaseGeometry class."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initializes a rectangle class"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the string representation of the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initializes a square class"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """returns the string representation of the square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
