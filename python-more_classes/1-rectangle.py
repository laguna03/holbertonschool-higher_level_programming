#!/usr/bin/python3
'''
Module for rectangle
'''
__width = None
__height = None


class Rectangle:
    '''Define a rectangle class'''

    def __init__(self, width=0, height=0):
        '''init function'''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise TypeError('Width must be >= 0')
        else:
            self.width = width
            if type(height) is not int:
                raise TypeError('Height ,ust be an integer')
            elif height < 0:
                raise TypeError('Heght must be >= 0')
            else:
                self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('Width value must be an integer')
        elif value < 0:
            raise ValueError('Width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('Height value must be an int')
        elif value < 0:
            raise ValueError('Height must must be 0<=')
        else:
            self.__height = value
