#!/usr/bin/python3
import unittest
#from models.rectangle import Rectangle
from rectangle import Rectangle
"""This module contains unittests for the rectangle.py module"""


class TestRectangle(unittest.TestCase):
    """A class for testing the Rectangle class"""

    def init_without_optional_arguments(self):
        """For testing the init method without optional arguments"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEquak(r1.width, 10)
        self.assertEqual(r1.height, 2)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)

    def init_with_optional_arguments(self):
        """For testing the init method with the optional arguments"""
