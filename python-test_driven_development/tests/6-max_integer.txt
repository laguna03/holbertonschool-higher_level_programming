#!/usr/bin/python3
"""Module to test"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class Test(unittest.TestCase):
    def test_max_int(self):
        max = max_integer([0, 1, 2, 3])
        self.assertEqual(max, 3)

    def test_nothing(self):
        max = max_integer([])
        self.assertEqual(max, None)

    def test_negatives(self):
        max = max_integer([-10, -11, -22, -6, -33, -40])
        self.assertEqual(max, -6)

    def test_negatives_positives(self):
        max = max_integer([-10, -11, -22, -6, -33, 3,-40])
        self.assertEqual(max, 3)

    def test_one_element(self):
        max = max_integer([1])
        self.assertEqual(max, 1)

    def test_max_beg(self):
        max = max_integer([1, 0])
        self.assertEqual(max, 1)

if __name__ == '__main__':
    unittest.main()
