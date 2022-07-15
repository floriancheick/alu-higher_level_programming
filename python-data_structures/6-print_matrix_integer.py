#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        level = 0
        for l in i:
            if level == (len(i) - 1):
                print("{:d}".format(l), end='')
            else:
                print("{:d}".format(l), end='')
                level += 1
                print("")
