#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix
    Args:
        matrix (list):
        div (int):

    Returns:
        A new matrix containing the results of the division

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats
        TypeError: If rows of matrix are not all the same size
        TypeError: If div is not an integer or float
        ZeroDivisionError: If div is 0
    """
    if not isinstance(matrix, list) and not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
