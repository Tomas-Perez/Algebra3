"""
Contains algorithms to solve Exercise 3
"""

import copy


"""
Calculates the product between a superior triangular matrix and a vector
"""


def exc3ai(matrix, vector):
    result = []
    matrix_size = len(matrix)
    for m in range(matrix_size):
        result.append(0)
        for n in range(m, matrix_size):
            result[m] += matrix[n][m] * vector[n]
    return result


"""
Calculates de sum between two superior triangular matrix
"""


def exc3aii(matrix1, matrix2):
    result = copy.deepcopy(matrix1)
    matrix_size = len(matrix1)
    current_start = 0
    for m in range(matrix_size):
        for n in range(current_start, matrix_size):
            result[n][m] += matrix2[n][m]
        current_start += 1
    return result


def exc3aiii(matrix1, matrix2):
    matrix_size = len(matrix1)
    result = [[0] * matrix_size for _ in range(matrix_size)]
    for n in range(matrix_size):
        for j in range(matrix_size):
            for k in range(matrix_size):
                result[n][k] += matrix1[n][j] * matrix2[j][k]
    return result

