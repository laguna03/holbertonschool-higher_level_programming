#!/usr/bin/python3
""" Base class """


class Base:
    """ Base class for all objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the Base class """
        if id is not None:
            self.id = id
        else:
            """ Increment the number of objects"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
