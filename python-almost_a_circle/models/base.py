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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                return [cls.create(**d) for d in cls.from_json_string(f.read())]
        except:
            return []
