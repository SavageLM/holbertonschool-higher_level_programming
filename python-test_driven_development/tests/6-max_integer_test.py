#!/usr/bin/python3
# 6-max_integer_test.py
# Logan Savage
"""Unit-test functions for max_integer()"""

import unittest
max_integer = __import__('6-max_integer').max_integer
"""importing the function and unitest functions"""

class TestMaxInteger(unitest.TestCase):
    """ Testing maz_integer"""

    def test_empty_list(self):
        """ Tests for empty lists"""
        no_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_empty_string(self):
        """ Tests for empty strings"""
        self.assertEqual(max_integer(""), None)

    def test_unsorted_list(self):
        """ Tests for unsorted lists"""
        unsort = [1, 9, 3, 6]
        self.assertEqual(max_integer(unsort), 9)

    def test_sorted_list(self):
        """ Tests for sorted lists"""
        sort = [1, 2, 6, 9]
        self.assertEqual(max_integer(sort), 9)

    def test_neg(self):
        """ Tests for negatives"""
        neg = [-8, -5, -3, -1]
        self.assertEqual(max_integer(neg), -1)

if __name__ == '__main__':
    unittest.main()
