from math import *


class Exercise2:
    """
    Contains algorithms for solving exercise 2
    """

    """
    Verifies if the matrix given is symmetrical
    """
    def exerciseA(self, matrix, calculator):
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True

    """
    Verifies if a given matrix is diagonally dominant
    """
    def exerciseB(self, matrix, calculator):
        comparator = 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if j != i:
                    comparator += matrix[i][j] ** 2
            if matrix[i][i] < sqrt(comparator):
                return False
        return True

"""
2a)
verifies if the matrix given is symmetrical
"""


def is_symmetrical(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

"""
2b)
verifies if a given matrix is diagonally dominant
"""


def is_dominant(matrix):
    comparator = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if j != i:
                comparator += matrix[i][j]**2
        if matrix[i][i] < sqrt(comparator):
            return False
    return True


# TODO @ariel need this?
def find_diagonal_min(matrix):
    result = matrix[0][0]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if result > matrix[i][j]:
                result = matrix[i][j]
    return result

