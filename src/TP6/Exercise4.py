class Exercise4:

    """
    Contains algorithms to solve exercise 4
    """

    """
    Takes two matrices stored in a linear array and returns their sum as a matrix
    """
    def summation(self, matrixA, matrixB, calculator):
        result = []
        matrix_size = len(matrixA)
        for x in range(matrix_size):
            result.append(calculator.sum(matrixA[x], matrixB[x]))
        return self.array_to_matrix(result)

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

    """
    Takes an array representing a superior triangular matrix and returns it as a proper matrix
    """
    def array_to_matrix(self, array):
        summation = 0
        matrix_len = 0
        for i in range(len(array)):
            summation += i
            if summation == len(array):
                matrix_len = i
                break
        result = [[0] * matrix_len for _ in range(matrix_len)]
        k = 0
        for i in range(matrix_len):
            for j in range(i, matrix_len):
                result[i][j] = array[k]
                k += 1
        return result

