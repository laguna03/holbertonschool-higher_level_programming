#!/usr/bin/python3
"""
This module provides a simple addition operation.

The function add_integer adds two numbers, which can be integers or floats.
If the input values are floats, they will be casted to integers before
addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if (not isinstance(a, (int, float))) or (a != a):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))) or (b != b):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
