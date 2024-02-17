import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base(unittest.TestCase):

    def test_change(self):
        b5 = Base()
        b5.id = 4
        self.assertEqual(b5.id, 4)

    def test_creates(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(10)
        self.assertEqual(b2.id, 10)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        self.assertNotEqual(b2.id, 2)

    def test_json_s(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(json_dictionary), str)
        self.assertNotEqual(dictionary, json_dictionary)

    def test_json_s_static(self):
        self.assertTrue(Base.__dict__.get("to_json_string"), staticmethod)

    def test_save_to_file_class(self):
        self.assertTrue(Base.__dict__.get("to_json_string"), classmethod)

    def test_save_to_file(self):
        Rectangle.save_to_file([])
        Rectangle.save_to_file(None)
        Rectangle.save_to_file([Rectangle(4, 6, 0, 0, 10)])
        # Square
        Square.save_to_file(None)
        Square.save_to_file([])
        Square.save_to_file([Square(4)])

    def test_from_json_string_class(self):
        self.assertTrue(Base.__dict__.get("from_json_string"), staticmethod)

    def test_from_json_string(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4},{'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

    def test_creates(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

    def test_load_from_file(self):
        Rectangle.load_from_file()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        # Square
        Square.load_from_file()
        s1 = Square(4)
        s2 = Square(6, 4, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()
