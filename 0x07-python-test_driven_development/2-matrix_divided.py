#!/usr/bin/python3
"""
A Module contains one function that outputs a new matrix.

"""


def matrix_divided(matrix, div):
    """ A Module contains one function that outputs a new matrix. """

    msg_list = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(msg_list)
    if not isinstance(matrix, list):
        raise TypeError(msg_list)

    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(msg_list)
        if len(rows) == 0:
            raise TypeError(msg_list)
        if len(rows) != len(matrix[0]):
            raise TypeError(msg_size)
        for element in rows:
            if not isinstance(element, (int, float)):
                raise TypeError(msg_list)
    mat = [[round(y/div, 2) for y in rows] for rows in matrix]
    return (mat)
