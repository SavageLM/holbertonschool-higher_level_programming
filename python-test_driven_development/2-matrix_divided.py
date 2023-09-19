#!/usr/bin/python3
# 2-matrix_divided.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that divides elements of a matrix by given value """


def matrix_divided(matrix, div):
    """Returns a new matrix wtih all elements divided by div
    
    Floats with be cast to int.

    Raises:
    TypeError if each row of matrix is not even
    TypeError if div is not an int or float
    TypeError if Matrix is not a list of lists containing ints or floats
    ZeroDivisionError if div is 0
    """

