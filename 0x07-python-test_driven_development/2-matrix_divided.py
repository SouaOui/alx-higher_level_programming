#!/usr/bin/python3
"""
Matrix function
"""


def matrix_divided(matrix, div):
    """
    Matrix Divide
    """
    new_matrix = []
    if matrix == []:
        return new_matrix
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    try:
        size = len(matrix[0])
    except Exception:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for item in matrix:
        if (not isinstance(item, list)):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(item) != size:
            raise TypeError("Each row of the matrix must \
have the same size")
        new_row = []
        for num in item:
            if (not isinstance(num, int) or not isinstance(num, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            num /= div
            num = round(num, 2)
            new_row.append(num)
        new_matrix.append(new_row)
    return (new_matrix)
