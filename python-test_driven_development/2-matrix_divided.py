#!/usr/bin/python3
"""
Module that contains the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div.
    Returns a new matrix with elements rounded to 2 decimal places.
    """
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(x, (int, float)) for x in row)
                    for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row]
            for row in matrix]
