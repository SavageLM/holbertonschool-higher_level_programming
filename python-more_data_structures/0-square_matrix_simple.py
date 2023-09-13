#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix.append(j * j)
    return new_matrix
