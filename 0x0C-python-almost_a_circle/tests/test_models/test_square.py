#!/usr/bin/python3
import unittest
#from models.square import Square
#from models.square import Base
#from models.rectangle import Rectangle
from square import Square
from rectangle import Rectangle
from base import Base
"""This module contains unittests for the square.py module"""


class TestSquare(unittest.TestCase):
    """A class for testing the Rectanlge class"""

    def testing_instatiation(self):
        """Tests the instatiation of the Square Class"""
        self.assertIsInstance(Square(3, 1, 1), Base)
        self.assertIsInstance(Square(2, 1, 1), Rectangle)

    def testing_exceptions_in_initialization(self):
        """Tests exceptions in object's initialization"""
        self.assertRaises(TypeError, Square, "Hello")
        self.assertRaises(ValueError, Square, -1)

        """Testing x and y attributes"""
        self.assertRaises(TypeError, Square, 1, [])
        self.assertRaises(TypeError, Square, 1, 1, {})
        self.assertRaises(ValueError, Square, 1, 0)
        self.assertRaises(ValueError, Square, 1000, 5000, -1000)

    def testing_getters(self):
        """Tests the getters methods"""
        s1 = Square(10, 1, 1, 50)

        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 50)

    def testing_area_method(self):
        """Testing the area method"""
        s1 = Square(4, 1, 1)
        self.assertEqual(s1.area(), 16)

    def testing_large_area_method(self):
        """Testing the area method for modified values"""
        s1 = Square(99999999999999, 1, 1)
        s1.width = 500
        s1.height = 500
        self.assertEqual(s1.area(), 250000)

    def testing_size_methods(self):
        """Testing the size getters and setters"""
        s1 = Square(1, 1, 1)

        s1.size = 5
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.area(), 25)
