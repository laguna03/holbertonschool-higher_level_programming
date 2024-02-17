import unittest
from models.square import Square
class Test_Base(unittest.TestCase):


    def test_creates_square(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 =Square(5, 5)
        self.assertEqual(s2.x, 5)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.y, 3)
        s3 = Square(3, 1, 3, 2)
        print(s3)
        print(s3.area())

    def test_str_(self):
        self.assertEqual(Square(2, 0, 0, 20).__str__(), "[Square] (20) 0/0 - 2")

    def test_display_s(self):
        with self.assertRaises(TypeError):
            Square.display()
        with self.assertRaises(TypeError):
            Square(4, None).display()
        with self.assertRaises(TypeError):
            Square.display()
        s2 = Square(2, 4, 0, 20)
        self.assertEqual(s2.display(), 0)
        self.assertEqual(Square(5, 4, 40).display(), 0)

    def test_raise_value_error_square(self):
        with self.assertRaises(ValueError):
            Square(0, 1, 3)
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(ValueError):
            Square(5, -5)
        with self.assertRaises(ValueError):
            Square(5, 5, -5)

    def test_raise_type_error_square(self):
        with self.assertRaises(TypeError):
            Square("b")
        with self.assertRaises(TypeError):
            Square(5, "b")
        with self.assertRaises(TypeError):
             Square(5, 5, "b")
        # with self.assertRaises(TypeError):
        #     Square(5, 5, 5, "b")
        with self.assertRaises(TypeError):
            s1 = Square(5)
            s1.size = "9"


    def test_update(self):
        s1 = Square(5)
        s1.update(size=7, y=1)
        print(s1)
        s1.update(1, 2, 3)
        print(s1)

    def test_to_dictionary(self):
        s1 = Square(10, 2, 2, 2)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 2, 'x': 2, 'size': 10, 'y': 2})

    def test_load_from_file_s(self):
     # Square
        Square.load_from_file()
        s1 = Square(4)
        s2 = Square(6, 4, 4)
        list_square_input = [s1, s2]
        Square.save_to_file(list_square_input)
        list_square_output = Square.load_from_file()

    def test_save_to_file_s(self):
        self.assertEqual(Square.save_to_file(None), 0)
        self.assertEqual(Square.save_to_file([]), 0)
        Square.save_to_file([Square(4)])
