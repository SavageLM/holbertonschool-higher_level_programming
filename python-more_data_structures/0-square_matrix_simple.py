#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    power = lambda x, y: x**y
    new_matrix = []
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix.append(power(j, 2))
    return new_matrix
