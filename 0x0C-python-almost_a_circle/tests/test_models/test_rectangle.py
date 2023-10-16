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
        r1 = Rectangle(10, 2, 4, 5, 6)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 6)

        r1.width = 1000
        r1.height = 57689
        r1.x = 5869
        r1.y = 958
        r1.id = 958

        self.assertEqual(r1.width, 1000)
        self.asserEqual(r1.height, 57689)
        self.assertEqual(r1.x, 5869)
        self.assertEqual(r1.y, 958)
        self.assertEqual(r1.id, 958)

    def testing_exceptions(self):
        """For testing methods exceptions"""
        r1 = Rectangle(10, 45, 68, 958, 5)

        self.assertRaises(TypeError, r1.width, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-45, 10)

        self.assertRaises(TypeError, r1.height, "hello")
        self.assertRaises(ValueError, Rectangle, 10, -5)

        self.assertRaises(TypeError, r1.x, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 0, -4)

        self.assertRaises(TypeError, r1.y, [])
        self.assertRaises(ValueError, Rectangle, 10, 2, 4, -1000)
