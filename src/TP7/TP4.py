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

    # Returns double[]
    def exercise5WithoutPivoteo(self, coefficients, independent_terms):
        # Implement algorithm
        return 

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise5PartialPivoteo(self, coefficients, independent_terms):
        # Implement algorithm
        return 

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

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[]. 
    def exercise9(self, coefficients, independent_terms):
        # Implement algorithm
        return