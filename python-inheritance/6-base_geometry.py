#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
