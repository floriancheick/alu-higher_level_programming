#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for l in range(len(matrix[i])):
            if l != 0:
                print(" ", end='')
                print("{:d}".format(matrix[i][l]), end='')
                print()
