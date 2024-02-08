#!/usr/bin/python3
'''
Module for rectangle
'''
__width = None
__height = None


class Rectangle:
    '''Define a rectangle class'''

    def __init__(self, height=0, width=0):
        '''init function'''
        if type (height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise TypeError('height must be >= 0')
        else:
            self.height = height

            if type(width) is not int:
                raise TypeError('width ,ust be an integer')
            elif width < 0:
                raise TypeError('width must be >= 0')
            else:
                self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('Width value must be an integer')
        elif value < 0:
            raise ValueError('Width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('Height value must be an int')
        elif value < 0:
            raise ValueError('Height must must be 0<=')
        else:
            self.__height = value
