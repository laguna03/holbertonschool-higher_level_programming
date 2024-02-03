#!/usr/bin/python3
"""
    module matrix_divided
"""


def matrix_divided(matrix, div):
    """
        matrix_divided: divide all elements of one list
    """
    result = []
    row = []

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(0, len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            row.append(round(j / div, 2))
        result.append(row)
        row = []
    return result
