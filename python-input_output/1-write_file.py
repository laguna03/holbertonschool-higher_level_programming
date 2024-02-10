#!/usr/bin/python3
""" Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """ Writes a string to a text file."""
    with open(filename, "w") as f:
        return f.write(text)
