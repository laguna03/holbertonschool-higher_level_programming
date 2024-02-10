#!/usr/bin/python3
""" File I/O print text file"""


def read_file(filename=""):
    """ Read text file and print it."""
    with open(filename, mode="r", encoding='utf-8') as f:
        print(f.read(), end="")
