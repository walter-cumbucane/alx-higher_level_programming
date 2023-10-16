#!/usr/bin/python3
import unittest
#from models.base import Base
from base import Base
"""This module contains unittests for the base.py module"""


class TestBase(unittest.TestCase):
    """A class for testing the Base class"""

    def test_init_with_none(self):
        """Tests when the object is initialized without arguments"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_init_with_arguments(self):
        """Tests when the object is initialized with arguments"""
        b1 = Base(4)
        b2 = Base(-5000)
        b3 = Base(10000000)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, -5000)
        self.assertEqual(b3.id, 10000000)
