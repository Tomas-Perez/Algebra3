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
    for n in range(matrix_size):
        result.append(0)
        for m in range(n, matrix_size):
            result[n] += matrix[n][m] * vector[m]
    return result


"""
Calculates the sum between two superior triangular matrix
"""


def exc3aii(matrix1, matrix2):
    result = copy.deepcopy(matrix1)
    matrix_size = len(matrix1)
    for n in range(matrix_size):
        for m in range(n, matrix_size):
            result[n][m] += matrix2[n][m]
    return result

"""
Calculates the product between two superior triangular matrix
"""


def exc3aiii(matrix1, matrix2):
    matrix_size = len(matrix1)
    result = [[0] * matrix_size for _ in range(matrix_size)]
    for n in range(matrix_size):
        for m in range(n, matrix_size):
            for i in range(m, matrix_size):
                result[n][i] += matrix1[n][m] * matrix2[m][i]
    return result

