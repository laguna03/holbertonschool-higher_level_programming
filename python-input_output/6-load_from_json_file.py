#!/usr/bin/python3
"""" Functions that creates an Object form a JSON File """
import json


def load_from_json_file(filename):
    """ Loads a JSON File"""
    with open(filename, 'r') as f:
        return json.load(f)
