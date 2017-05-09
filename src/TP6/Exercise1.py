"""
Contains algorithms for solving Exercise 1
"""


"""
Calculates the sum of the diagonal of a square matrix
"""


def diag_sum(matrix):
    matrix_size = len(matrix)
    result = 0
    for i in range(matrix_size):
        result += matrix[i][i]
    return result


"""
Calculates the sum of the diagonal of a square matrix
"""


def secondary_diag_sum(matrix):
    matrix_size = len(matrix)
    result = 0
    for i in range(matrix_size):
        result += matrix[matrix_size-i][i]
    return result


"""
creates an array in which each element is the sum of every row of a rectangular matrix
"""


def ex1c(matrix):
    result = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i] += matrix[i][j]
    return result

