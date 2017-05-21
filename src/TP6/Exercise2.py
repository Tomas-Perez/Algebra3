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
                    comparator = calculator.sum(comparator, calculator.multiplication(matrix[i][j], matrix[i][j]))
            if matrix[i][i] < sqrt(comparator):
                return False
        return True