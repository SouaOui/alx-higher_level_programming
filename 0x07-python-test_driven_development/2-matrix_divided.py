#!/usr/bin/python3
"""
Matrix function
"""
def matrix_divided(matrix, div):
    """
    Matrix Divide
    """
    for item in matrix:
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for item in matrix:
        for num in item:
            num /= div
            num = round(num, 2)
    return (matrix)