"""
Contains algorithms for solving Exercise 1
"""


"""
Calculates the sum of the diagonal of a square matrix
"""
import copy


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
        result += matrix[matrix_size-(i+1)][i]
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


"""
1d)
Calculates the product of a matrix A size n*m and a vector b size m
"""


def vector_matrix_product(matrix, vector):
    result = []
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i] * vector[j]
        result.append(sum)
    return result


"""
1f)
Calculates the product of two matrix if possible
"""


def matrix_product(matrixA, matrixB):
    if(len(matrixA[0]) != len(matrixA)):
        print("Product not possible")
        return None
    result = []
    for i in range(len(matrixA[0])):
        result.append([])
        for k in range(len(matrixB[0])):
            sum = 0
            for j in range(len(matrixA)):
                sum += matrixA[i][j] * matrixB[j][k]
            result[i].append(sum)
    return result


def transpose_matrix(matrix):
    result = []
    for m in range(len(matrix[0])):
        result.append([])
        for n in range(len(matrix)):
            result[m].append(matrix[n][m])
    return result
