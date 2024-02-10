#!/usr/bin/python3
"""
Task 1 - Write a class MyList that inherits from list
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
            """
            Print a sorted list
            """
            sorted_list = sorted(self)
            print(sorted_list)
