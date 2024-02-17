#!/usr/bin/python3
"""
    Write the class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
        This class creates a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Args:
                width (int): is the width of the rectangle
                height (int): is the height of the rectangle
                x: is the x position of the rectangle
                y: is the y position of the rectangle
                id(int): is the identification of rectangle

        """
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
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
            return the rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """
            prints the area of the rectangle with #
        """
        for y_1 in range(self.__y):
            print()
        for n in range(self.__height):
            for x_1 in range(self.__x):
                print(' ', end='')
            for m in range(self.__width):
                print("#", end='')
            print()
        return 0

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
            update the values of a rectangle.
        """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == 'x':
                    self.__x = v
                if k == 'y':
                    self.__y = v
                if k == 'width':
                    self.__width = v
                if k == 'height':
                    self.__height = v
                if k == 'id':
                    self.id = v

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        dict_i = {}
        dict_i['x'] = self.__x
        dict_i['y'] = self.__y
        dict_i['id'] = self.id
        dict_i['width'] = self.__width
        dict_i['height'] = self.__height
        return dict_i
