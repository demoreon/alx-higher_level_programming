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

    new_matrix = []
    for rows in matrix:
        if not isinstance(rows, list):
            raise TypeError(msg_list)
        if len(rows) == 0:
            raise TypeError(msg_list)
        if len(rows) != len(matrix[0]):
            raise TypeError(msg_size)

        new = []
        for item in rows:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_list)
            if item == float('inf') or item == -float('inf') or item != item:
                new.append(10.0)
        new_matrix.append(new)
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    mat = [[round(y/div, 2) for y in rows] for rows in new_matrix]
    return (mat)
