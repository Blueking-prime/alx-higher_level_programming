#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unit test for the max_integer function"""

    def test_regular(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)

    def test_multiple_maxs(self):
        self.assertAlmostEqual(max_integer([1, 3, 3]), 3)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_float(self):
        self.assertAlmostEqual(max_integer([3.9, 3.2, 3.6]), 3.9)

    def test_negative(self):
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)

    def test_negative_with_zero(self):
        self.assertAlmostEqual(max_integer([-1, 0, -3]), 0)

    def test_with_int(self):
        self.assertRaises(TypeError, max_integer, 5)

    def test_with_tuple(self):
        self.assertRaises(TypeError, max_integer, (8, 9, 'iu'))

    def test_list_containing_string(self):
        self.assertRaises(TypeError, max_integer, [8, 9, 'iu'])

if __name__ == '__main__':
    unittest.main()
