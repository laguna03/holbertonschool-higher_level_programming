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
        if id is None:
            self.id = Base().id
        else:
            self.id = id
            Base().id += 1

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

            """ Returns the area value of the Rectangle instance """
            return self.__width * self.__height

    def display(self):

        """ Prints in stdout the Rectangle instance with the character # """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):

            """ Returns the string representation of the Rectangle instance """
            return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):

        """ Assigns an argument to each attribute """
        if args:
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
            for key, value in kwargs.items():
                setattr(self, key, value)
