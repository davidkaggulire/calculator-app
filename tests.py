"""test.py"""

import unittest
from calculator import add_function, multiplication_function, subtract_function, division_function, remainder_function


class TestCalculator(unittest.TestCase):
    """test class for calculator"""

    def test_addition(self):
        """tests for addition function"""
        assert 4 == add_function(2, 2)

    def test_subtraction(self):
        """test to check subtraction"""
        assert 2 == subtract_function(4, 2)

    def test_multiply(self):
        """test to check for product function"""
        assert 8 == multiplication_function(2, 4)

    def test_divide(self):
        """test to check division function"""
        assert 2 == division_function(6, 3)

    def test_remainder(self):
        """test to check remainder"""
        assert 1 == remainder_function(5, 2)
