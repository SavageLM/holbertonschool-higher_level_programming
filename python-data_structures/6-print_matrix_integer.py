#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    flag = 0
    for i in matrix:
        for j in i:
            if flag != 0:
                print(" ", end='')
            print("{:d}".format(j), end='')
            flag = 1
        print()
        flag = 0
