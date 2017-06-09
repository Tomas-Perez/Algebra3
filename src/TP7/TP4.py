import copy


class TP4:

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise1(self, coefficients, independent_terms):
        # Implement algorithm
        return 

    # Returns double[]. coefficients is of type double[][]. independentTerms is of type double[].
    def exercise2(self, coefficients, independent_terms):
        # Implement algorithm
        return 

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