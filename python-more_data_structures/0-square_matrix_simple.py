#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        squared_matrix.append(list(map(lambda x: x**2, row)))
    return squared_matrix
