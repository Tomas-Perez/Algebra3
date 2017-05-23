class TP4:

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise1(self, coefficients, independent_terms):
        # Implement algorithm
        return 

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise2(self, coefficients, independent_terms):
        # Implement algorithm
        return 

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