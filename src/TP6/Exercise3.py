import copy


class Exercise3:
    """
    Contains algorithms to solve Exercise 3
    """

    """
    Calculates the product between a superior triangular matrix and a vector
    """
    def exerciseAI(self, matrixA, vectorX, calculator):
        result = []
        matrix_size = len(matrixA)
        for n in range(matrix_size):
            result.append(0)
            for m in range(n, matrix_size):
                multiplication = calculator.multiplication(matrixA[n][m], vectorX[m])
                result[n] = calculator.sum(result[n], multiplication)
        return result

    """
    Calculates the sum between two superior triangular matrix
    """
    def exerciseAII(self, matrixA, matrixB, calculator):
        result = copy.deepcopy(matrixA)
        matrix_size = len(matrixA)
        for n in range(matrix_size):
            for m in range(n, matrix_size):
                result[n][m] = calculator.sum(result[n][m], matrixB[n][m])
        return result

    """
    Calculates the product between two superior triangular matrix
    """
    def exerciseAIII(self, matrixA, matrixB, calculator):
        matrix_size = len(matrixA)
        result = [[0] * matrix_size for _ in range(matrix_size)]
        for n in range(matrix_size):
            for m in range(n, matrix_size):
                for i in range(m, matrix_size):
                    multiplication = calculator.multiplication(matrixA[n][m], matrixB[m][i])
                    result[n][i] = calculator.sum(result[n][i], multiplication)
        return result

    # Returns double[][]; matrixA is of type double[][]; vectorX is of type double[]; calculator is of type Calculator
    def exerciseBI(matrixA, vectorX, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseBII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseBIII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; vectorX is of type double[]; calculator is of type Calculator
    def exerciseCI(matrixA, vectorX, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseCII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseCIII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; vectorX is of type double[]; calculator is of type Calculator
    def exerciseDI(matrixA, vectorX, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseDII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseDIII(matrixA, matrixB, calculator):
        # Implement
        return

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseE(matrixA, matrixB, calculator):
        # Implement
        return


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

