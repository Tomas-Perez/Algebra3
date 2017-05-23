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
        # Implement algorithm
        return 

    # Returns double[][]. coefficients is of type double[][].
    def exercise8(self, coefficients):
        # Implement algorithm
        return 

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[]. 
    def exercise9(self, coefficients, independent_terms):
        # Implement algorithm
        return