#!/usr/bin/python3
""" Function that writesan object a text file, using a JSON representation. """
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writesan object a text file,
    using a JSON representation.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
