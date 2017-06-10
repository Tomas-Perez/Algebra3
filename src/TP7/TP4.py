import copy


class TP4:
    """
    Contains algorithms to solve Exercise 1,2,5,6,7,8,9 from tp7
    """

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise1(self, coefficients, independent_terms):
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
        length = len(coefficients)
        n = length - 1
        result = [0] * length
        result[0] = independent_terms[0]/coefficients[0][0]
        for i in range(1, length):
            product = 0
            for j in range(0, i):
                product += coefficients[i][j] * result[j]
            result[i] += (independent_terms[i] - product)/coefficients[i][i]
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


    # Returns double[]
    def exercise5WithoutPivoteo(self, coefficients, independent_terms):
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        n = len(coefficients)
        self.gauss_system(a, b)
        return self.exercise1(a, b)


    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise5PartialPivoteo(self, coefficients, independent_terms):
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        n = len(coefficients)
        self.gauss_system(a, b, self.partial_pivot())
        return self.exercise1(a, b)

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise6(self, coefficients, independent_terms, calculator):
        # Implement algorithm
        return 

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise7(self, coefficients, independent_terms, calculator):
        return

    # Returns double[][]. coefficients is of type double[][].
    def exercise8(self, coefficients):
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

    def lu_decomposition(self, A):
        """Performs an LU Decomposition of a matrix (which must be square)                                                                                                                                                                                        
        into coefficients = LU. The function returns L and U."""
        n = len(A)

        # Create zero matrices for L and U
        L = [[0.0] * n for i in range(n)]
        U = [[0.0] * n for i in range(n)]

        # Perform the LU Decomposition
        for j in range(n):
            # All diagonal entries of L are set to 1, because is Doolitle algorithm
            L[j][j] = 1.0

            # LaTeX: u_{ij} = a_{ij} - \sum_{k=1}^{i-1} u_{kj} l_{ik}
            for i in range(j + 1):
                s1 = sum(U[k][j] * L[i][k] for k in range(i))
                U[i][j] = A[i][j] - s1

            # LaTeX: l_{ij} = \frac{1}{u_{jj}} (a_{ij} - \sum_{k=1}^{j-1} u_{kj} l_{ik} )
            for i in range(j, n):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A[i][j] - s2) / U[j][j]

        return L, U

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[]. 
    def exercise9(self, coefficients, independent_terms):
        # implement
        return



