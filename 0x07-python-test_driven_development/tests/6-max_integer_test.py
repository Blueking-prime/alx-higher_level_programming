"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def regular_test(self):
        '''Tests normal use cases'''
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 3, 3]), 3)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([3.9, 3.2, 3.6]), 3.9)

    def negative_test(self):
        '''tests when list contains negative values'''
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
        self.assertAlmostEqual(max_integer([-1, 0, -3]), 0)

    def type_error_checks(self):
        '''Checks if program returns known type errors'''
        self.assertRaises(TypeError, max_integer, 'str')
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, (8, 9, 'iu'))

    def value_error_checks(self):
        '''Checks if program returns known type errors'''
        self.assertRaises(ValueError, max_integer, [8, 9, 'iu'])
        self.assertRaises(ValueError, max_integer, ['iu'])
