#!/usr/bin/python3

class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the Base class """
        if id is not None:
            self.id = id
        else:
            """ Increment the number of objects"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
