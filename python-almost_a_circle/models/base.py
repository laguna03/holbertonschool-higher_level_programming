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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))
