#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        for col in range(len(row)):
            square = row[col] ** 2
            square_matrix.append(square)
    return square_matrix
