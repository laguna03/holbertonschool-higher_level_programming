#!/usr/bin/python3

""" unittest for Rectangle([..]) """

import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """Unitests for Rectangle"""

    def test_empty(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_multiple_instances(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_set_id(self):
        r4 = Rectangle(89, 1)
        self.assertEqual(r4.id, 89)

    def test_set_width(self):
        r5 = Rectangle(10, 2)
        self.assertEqual(r5.width, 10)

    def test_set_height(self):
        r6 = Rectangle(10, 2)
        self.assertEqual(r6.height, 2)

    def test_set_x(self):
        r7 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r7.x, 0)

    def test_set_y(self):
        r8 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r8.y, 0)

    def test_set_width_type(self):
        with self.assertRaises(TypeError):
            r9 = Rectangle("10", 2)

    def test_set_height_type(self):
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, "2")

    def test_set_x_type(self):
        with self.assertRaises(TypeError):
            r11 = Rectangle(10, 2, "0", 0, 12)

    def test_set_y_type(self):
        with self.assertRaises(TypeError):
            r12 = Rectangle(10, 2, 0, "0", 12)

    def test_set_width_value(self):
        with self.assertRaises(ValueError):
            r13 = Rectangle(-10, 2)

    def test_set_height_value(self):
        with self.assertRaises(ValueError):
            r14 = Rectangle(10, -2)

    def test_set_x_value(self):
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, 2, -1, 0, 12)

    def test_set_y_value(self):
        with self.assertRaises(ValueError):
            r16 = Rectangle(10, 2, 0, -1, 12)

    def test_area(self):
        r17 = Rectangle(10)
