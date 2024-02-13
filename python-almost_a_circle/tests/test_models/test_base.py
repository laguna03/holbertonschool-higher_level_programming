#!/usr/bin/python3
"""
    Unittest for Base([..])
"""
import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """Unitests for Base"""
    def test_empty(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_multiple_instances(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)

    def test_set_id(self):
        b5 = Base(89)
        self.assertEqual(b5.id, 89)

if __name__ == '__main__':
    unittest.main()
