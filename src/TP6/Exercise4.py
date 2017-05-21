class Exercise4:

    """
    Contains algorithms to solve exercise 4
    """

    """
    Takes two matrices stored in a linear array and returns their sum
    """
    def summation(self, matrixA, matrixB, calculator):
        result = []
        matrix_size = len(matrixA)
        for x in range(matrix_size):
            result.append(calculator.sum(matrixA[x], matrixB[x]))
        return result

    """
    Takes a superior triangular matrix and returns it as an array
    """
    def matrix_to_array(self, matrix):
        result = []
        matrix_size = len(matrix)
        for n in range(matrix_size):
            for m in range(n, matrix_size):
                result.append(matrix[n][m])
        return result
