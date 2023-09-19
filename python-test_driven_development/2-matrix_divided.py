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

    ermo = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(ermo)
    if all(len(row) == len(matrix[0]) for row in matrix) is not True:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for ele in row:
            if type(ele) is not int and type(ele) is not float:
                raise TypeError(ermo)
            new_matrix[row].append(round(ele / div, 2))
    return new_matrix
