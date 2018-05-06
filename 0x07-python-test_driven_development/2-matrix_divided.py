#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if isinstance(matrix, list) is False:
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
    for row in matrix:
        if len(row) == len(matrix[0]):
            continue
        else:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for j in row:
            if isinstance(j, (int, float)) is False:
                raise TypeError(
                    "matrix must be a matrix (list of lists) " +
                    "of integers/floats")
            else:
                continue
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x/div, 2), i)))
    return new_matrix
