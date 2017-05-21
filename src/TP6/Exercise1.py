class Exercise1:
    """
    Contains algorithms for solving Exercise 1
    """

    """
    Calculates the sum of the diagonal of a square matrix
    """
    def exerciseA(self, matrix, calculator):
        matrix_size = len(matrix)
        result = 0
        for i in range(matrix_size):
            result += matrix[i][i]
        return result

    """
    Calculates the sum of the diagonal of a square matrix
    """
    def exerciseB(self, matrix, calculator):
        matrix_size = len(matrix)
        result = 0
        for i in range(matrix_size):
            result += matrix[matrix_size - (i + 1)][i]
        return result

    """
    Creates an array in which each element is the sum of every row of a rectangular matrix
    """
    def exerciseC(self, matrix, calculator):
        result = []
        row_result = 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                row_result = calculator.sum(row_result, matrix[i][j])
            result.append(row_result)
            row_result = 0
        return result

    """
    Calculates the product between a matrix A size n*m and a vector b size m
    """
    def exerciseD(self, matrix, vector, calculator):
        result = []
        for i in range(len(matrix[0])):
            sum = 0
            for j in range(len(matrix)):
                sum += calculator.multiplication(matrix[i][j],vector[j])
            result.append(sum)
        return result

    """
    Calculates the sum between two n*m matrices if possible
    """
    def exerciseE(self, matrixA, matrixB, calculator):
        if len(matrixA[0]) != len(matrixB[0]) or len(matrixA) != len(matrixB):
            print("sum not possible")
            return None
        result = []
        for n in range(len(matrixA[0])):
            result.append([])
            for m in range(len(matrixB[0])):
                sum = calculator.sum(matrixA[n][m], matrixB[n][m])
                result[n].append(sum)
        return result

    """
    Calculates the product of two matrix if possible
    """
    def exerciseF(self, matrixA, matrixB, calculator):
        if len(matrixA[0]) != len(matrixA):
            print("Product not possible")
            return None
        result = []
        for i in range(len(matrixA[0])):
            result.append([])
            for k in range(len(matrixB[0])):
                sum = 0
                for j in range(len(matrixA)):
                    sum += calculator.multiplication(matrixA[i][j], matrixB[j][k])
                result[i].append(sum)
        return result

    """
    Takes a matrix and returns a transposed copy
    """
    def exerciseG(self, matrix, calculator):
        result = []
        for m in range(len(matrix[0])):
            result.append([])
            for n in range(len(matrix)):
                result[m].append(matrix[n][m])
        return result
