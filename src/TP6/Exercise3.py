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
    '''
    Calculates the product between a vector size n and a band n*n matrix 
    '''
    def exerciseDI(self, matrixA, vectorX, k1, k2, calculator):
        result =[]
        for i in range(len(matrixA[0])):
            sum = 0
            r = (j for j in range(i-k1, i+k2) if 0 <= j < len(matrixA))
            for j in range(r):
                sum += calculator.multiplication(matrixA[i][j], vectorX[j])
            result[i] = sum
        return result

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    '''
    Calculates the sum between a band n*n matrix and another matrix
    '''
    def exerciseDII(self, matrixA, matrixB, k1, k2, calculator):
        length = len(matrixA)
        result = [[0] * length for _ in range(length)]
        for i in range(len(matrixA[0])):
            for j in range(len(matrixA)):
                if i+k2 >= j >= i-k1:
                    result[i][j] = calculator.sum(matrixA[i][j], matrixB[i][j])
                else:
                    result[i][j] = matrixB[i][j]
        return result

    # Returns double[][]; matrixA is of type double[][]; matrixB is of type double[][]; calculator is of type Calculator
    def exerciseDIII(self, matrixA, matrixB, k1, k2, calculator):
        result = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]
        for i in range(len(matrixA[0])):
            for k in range(len(matrixB[0])):
                sum = 0
                r = (j for j in range(i-k1, i+k2+1) if 0 <= j < len(matrixA))
                for j in r:
                    sum += calculator.multiplication(matrixA[i][j], matrixB[j][k])
                result[i][k] = sum
        return result

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

