#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    one = []
    for i in matrix:
        one.append([j ** 2 for j in i])
        return one
