#!/usr/bin/python3
"""
print square
"""


def print_square(s):
    """print square - S is Size"""
    if type(s) is not int or type(s) is float and s < 0:
        raise TypeError("size must be an integer")
    elif s < 0:
        raise ValueError("size must be >= 0")
    if s != 0:
        print('\n'.join([''.join('#' * s)] * s))
