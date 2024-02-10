#!/usr/bin/python3
"""
Task 1 - Write a class MyList that inherits from list
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
