#!/usr/bin/python3
'''Class Square'''


class Square:
    '''Size and error check for Square'''

    def __init__(self, size=0):


        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self._size = size
