#!/usr/bin/python3
""" Say my name module """


def say_my_name(first_name, last_name=""):
    """ prints full name by user input """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
