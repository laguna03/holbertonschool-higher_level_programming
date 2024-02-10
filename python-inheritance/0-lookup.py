#!/usr/bin/python3
"""
Task 0 - Function which return the list of all available
attributes and methods of an object
"""


def lookup(obj):
    """
    Lookup receibe obj and return all atributes and methods of obj
    """

    return dir(obj)
