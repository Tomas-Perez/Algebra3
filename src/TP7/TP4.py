import copy
from cmath import e
class TP4:
    """
    Contains algorithms to solve Exercise 1,2,5,6,7,8,9 from tp7
    """

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise1(self, coefficients, independent_terms):
        """calculates unitary Ux=b"""
        length = len(coefficients)
        n = length - 1
        result = [0] * length
        result[n] = independent_terms[n]
        for i in range(n-1, -1, -1):
            product = 0
            for j in range(i+1, length):
                product += coefficients[i][j]*result[j]
            result[i] += independent_terms[i] - product
        return result

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise2(self, coefficients, independent_terms):
        """calculates Lx=b"""
        length = len(coefficients)
        n = length - 1
        result = [0] * length
        result[0] = independent_terms[0]/coefficients[0][0]
        for i in range(1, length):
            product = 0
            for j in range(0, i):
                product += coefficients[i][j] * result[j]
            result[i] += (independent_terms[i] - product) / coefficients[i][i]
        return result

    def gauss_system(self, a, b, pivot=None):
        n = len(a)
        for k in range(n):
            if pivot:
                pivot(a, b, k)
            div = a[k][k]
            for j in range(k, n):
                a[k][j] = a[k][j]/div
            b[k] = b[k]/div
            for i in range(k+1, n):
                mult = a[i][k]
                for j in range(k, n):
                    a[i][j] = a[i][j] - mult*a[k][j]
                b[i] = b[i] - mult*b[k]

    def partial_pivot(self, a, b, row):
        max_index = row
        for i in range(row, len(a)):
            if a[i][row] > a[max_index][row]:
                max_index = i
        if row is not max_index:
            a[row], a[max_index] = a[max_index], a[row]
            b[row], b[max_index] = b[max_index], b[row]



    def exercise5WithoutPivoteo(self, coefficients, independent_terms):
        """
        Takes an equation system formed by a nxm coefficient matrix and an mx1 vector with independent terms. 
        Returns its result using the gauss algorithm.
        :param coefficients: nxm matrix
        :param independent_terms: mx1 vector
        :return: mx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        self.gauss_system(a, b)
        return self.exercise1(a, b)


    def exercise5PartialPivoteo(self, coefficients, independent_terms):
        """
        Takes an equation system formed by a nxm coefficient matrix and an mx1 vector with independent terms. 
        Returns its result using the gauss algorithm and partial pivot.
        :param coefficients: nxm matrix
        :param independent_terms: mx1 vector
        :return: mx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        self.gauss_system(a, b, self.partial_pivot)
        return self.exercise1(a, b)

    def gauss_upper_hessenberg(self, a, b, calculator):
        n = len(a)
        for k in range(n):
            div = a[k][k]
            for j in range(k, n):
                a[k][j] = calculator.division(a[k][j], div)
            b[k] = calculator.division(b[k], div)
            if k is not n-1:
                i = k+1
                mult = a[i][k]
                for j in range(k, n):
                    a[i][j] = calculator.subtraction(a[i][j], calculator.multiplication(mult, a[k][j]))
                b[i] = calculator.subtraction(b[i], calculator.multiplication(mult, b[k]))

    def exercise6(self, coefficients, independent_terms, calculator):
        """
        Takes an equation system formed by a nxm upper hessenberg coefficient matrix and an mx1 vector 
        with independent terms. Returns its result using the gauss algorithm.
        :param coefficients: nxm upper hessenberg matrix
        :param independent_terms: mx1 vector
        :return: mx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        self.gauss_upper_hessenberg(a, b, calculator)
        return self.exercise1(a, b)

    def gauss_cubic_spline(self, a, b, calculator):
        n = len(a)
        for k in range(n):
            div = a[k][k]
            a[k][k] = calculator.division(a[k][k], div)
            b[k] = calculator.division(b[k], div)
            if k <= n-2:
                i = k+1
                a[k][i] = calculator.division(a[k][i], div)
                mult = a[i][k]
                a[i][k] = calculator.subtraction(a[i][k], calculator.multiplication(mult, a[k][k]))
                if k <= n-3:
                    a[i][k+1] = calculator.subtraction(a[i][k+1], calculator.multiplication(mult, a[k][k+1]))
                b[i] = calculator.subtraction(b[i], calculator.multiplication(mult, b[k]))

    def solve_cubic_spline_after_gauss(self, coefficients, independent_terms, calculator):
        length = len(coefficients)
        n = length - 1
        result = [0] * length
        result[n] = independent_terms[n]
        for i in range(n-1, -1, -1):
            product = 0
            for j in range(i+1, min(i+3, length)):
                product = calculator.sum(product, calculator.multiplication(coefficients[i][j], result[j]))
            result[i] = calculator.sum(result[i], calculator.subtraction(independent_terms[i], product))
        return result

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise7(self, coefficients, independent_terms, calculator):
        """
        Takes an equation system formed by a nxm cubic spline coefficient matrix and an mx1 vector 
        with independent terms. Returns its result using the gauss algorithm.
        :param coefficients: nxm upper hessenberg matrix
        :param independent_terms: mx1 vector
        :return: mx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        self.gauss_cubic_spline(a, b, calculator)
        return self.solve_cubic_spline_after_gauss(a, b)

    # Returns double[][]. coefficients is of type double[][].
    def exercise8(self, coefficients):
        """
        Calculates the inverse matrix of the received matrix using the Gauss-Jordan algorithm
        :param coefficients: nxm matrix
        :return: nxm matrix that is the calculated inverse
        """
        length = len(coefficients[0])
        for i in range(length):
            for j in range(length):
                if i == j:
                    coefficients[i].append(1)
                else:
                    coefficients[i].append(0)
        for k in range(length):
            firstValue = coefficients[k][k]
            # fila paso 1.
            for j in range(k, length + 1 + k):
                coefficients[k][j] /= firstValue
            #paso 2
            for i in range(length):
                if i != k:
                    firsRowValue = coefficients[i][k]
                    for j in range(k, length + 1 + k):
                        coefficients[i][j] -= firsRowValue * coefficients[k][j]
        inverse = []
        for i in range(length):
            inverse.append([])
            for j in range(length, length*2):
                inverse[i].append(coefficients[i][j])
        return inverse

    def doolitle_decomposition(self, A, L, U):
        """Performs an LU Decomposition of a matrix (which must be square)                                                                                                                                                                                        
        into coefficients = LU. The function returns L and U."""
        n = len(A)

        # Create zero matrices for L and U
        for i in range(n):
            for j in range(n):
                L[i][j] = 0
                U[i][j] = 0

        # LU doolitle Decomposition
        for j in range(n):
            # All diagonal entries of L are set to 1, because is Doolitle algorithm
            L[j][j] = 1.0

            for i in range(j + 1):
                s1 = sum(U[k][j] * L[i][k] for k in range(i))
                U[i][j] = A[i][j] - s1

            for i in range(j, n):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A[i][j] - s2) / U[j][j]

    def crout_decomposition(self, A, L, U):
        n = len(A)

        # Create zero matrices for L and U
        for i in range(n):
            for j in range(n):
                L[i][j] = 0
                U[i][j] = 0

        # LU crout Decomposition
        for j in range(n):
            U[j][j] = 1  # set the j,j-th entry of U to 1
            for i in range(j, n):  # starting at L[j][j], solve j-th column of L
                alpha = float(A[i][j])
                for k in range(j):
                    alpha -= L[i][k] * U[k][j]
                L[i][j] = alpha
            for i in range(j + 1, n):  # starting at U[j][j+1], solve j-th row of U
                tempU = float(A[j][i])
                for k in range(j):
                    tempU -= L[j][k] * U[k][i]
                if int(L[j][j]) == 0:
                    L[j][j] = e - 40
                U[j][i] = tempU / L[j][j]

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[]. 
    def exercise9(self, A, independent_terms, L, U):
        self.crout_decomposition(A, L, U)
        z = self.exercise2(L, independent_terms)
        x = self.exercise1(U, z)
        return x



