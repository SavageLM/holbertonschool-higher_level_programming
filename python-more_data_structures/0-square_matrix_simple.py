#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    sqr_matrix = []
    for i in range(len(matrix)):
        sqr_matrix.append([])
        for j in matrix[i]:
            sqr_matrix.append(j * j)
    return sqr_matrix
