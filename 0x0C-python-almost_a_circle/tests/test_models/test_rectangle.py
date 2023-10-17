#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""This module contains unittests for the rectangle.py module"""


class TestRectangle_instantiation(unittest.TestCase):
    """A class for testing the Rectangle instances"""

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

    def testing_small_ara(self):
        """Testing the area for small values"""
        r1 = Rectangle(3, 5, 1, 1)
        self.assertEqual(r1.area(), 15)

    def testing_large_area(self):
        """Testing the area for large values"""
        r1 = Rectangle(999999999999999, 999999999999999999, 1, 1)
        self.assertEqual(r1.area(), 999999999999998999000000000000001)

    def testing_area_changed_attributes(self):
        """Testing the area when attributes are changed"""
        r1 = Rectangle(3, 5, 1, 1, 1)
        r1.width = 4
        r1.height = 7
        self.assertEqual(r1.area(), 28)

    def testing_update_0(self):
        """Testing the version 1 of the update method"""
        r1 = Rectangle(10, 10, 10, 10)

        """Testing width"""
        r1.update(1, 3)
        self.assertEqual(r1.width, 3)
        self.assertRaises(TypeError, r1.update, 1, "Hello")
        self.assertRaises(ValueError, r1.update, 1, 0)

        """Testing height"""
        r1.update(1, 3, 5)
        self.assertEqual(r1.height, 5)
        self.assertRaises(TypeError, r1.update, 1, 3, tuple())
        self.assertRaises(ValueError, r1.update, 1, 3, -1000)

        """Testing X"""
        r1.update(1, 3, 5, 1)
        self.assertEqual(r1.x, 1)
        self.assertRaises(TypeError, r1.update, 1, 3, 5, dict())
        self.assertRaises(ValueError, r1.update, 1, 3, 5, -1)

        """Testing y"""
        r1.update(1, 3, 5)
        self.assertEqual(r1.height, 5)
        self.assertRaises(TypeError, r1.update, 1, 3, 5, 1, set())
        self.assertRaises(ValueError, r1.update, 1, 3, 5, 1, 0)

        def test_rectangle_is_base(self):
            self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)
