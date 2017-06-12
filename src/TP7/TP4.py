import copy
from cmath import e


def gauss_cubic_spline(a, b, calculator):
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


def gauss_system(a, b, pivot=None):
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


def partial_pivot(a, b, row):
    max_index = row
    for i in range(row, len(a)):
        if a[i][row] > a[max_index][row]:
            max_index = i
    if row is not max_index:
        a[row], a[max_index] = a[max_index], a[row]
        b[row], b[max_index] = b[max_index], b[row]


def gauss_upper_hessenberg(a, b, calculator):
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


def solve_cubic_spline_after_gauss(coefficients, independent_terms, calculator):
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


def doolittle_decomposition(a, l, u):
    """
    Performs an LU Decomposition of a nxn matrix into coefficients = LU.
    Using the doolittle algorithm. 
    :param a: nxn matrix to be decomposed
    :param l: L target nxn matrix
    :param u: U target nxn matrix
    :return: 
    """
    n = len(a)

    # Create zero matrices for L and U
    for i in range(n):
        for j in range(n):
            l[i][j] = 0
            u[i][j] = 0

    # LU doolittle Decomposition
    for j in range(n):
        # All diagonal entries of L are set to 1, because is Doolittle algorithm
        l[j][j] = 1.0

        for i in range(j + 1):
            s1 = sum(u[k][j] * l[i][k] for k in range(i))
            u[i][j] = a[i][j] - s1

        for i in range(j, n):
            s2 = sum(u[k][j] * l[i][k] for k in range(j))
            l[i][j] = (a[i][j] - s2) / u[j][j]


def crout_decomposition(a, l, u):
    """
    Performs an LU Decomposition of a nxn matrix into coefficients = LU.
    Using the crout algorithm. 
    :param a: nxn matrix to be decomposed
    :param l: L target nxn matrix
    :param u: U target nxn matrix
    :return: 
    """
    n = len(a)

    # Create zero matrices for L and U
    for i in range(n):
        for j in range(n):
            l[i][j] = 0
            u[i][j] = 0

    # LU crout Decomposition
    for j in range(n):
        u[j][j] = 1  # set the j,j-th entry of U to 1
        for i in range(j, n):  # starting at L[j][j], solve j-th column of L
            alpha = float(a[i][j])
            for k in range(j):
                alpha -= l[i][k] * u[k][j]
            l[i][j] = alpha
        for i in range(j + 1, n):  # starting at U[j][j+1], solve j-th row of U
            temp_u = float(a[j][i])
            for k in range(j):
                temp_u -= l[j][k] * u[k][i]
            if int(l[j][j]) == 0:
                l[j][j] = e - 40
            u[j][i] = temp_u / l[j][j]


class TP4:
    """
    Contains algorithms to solve Exercise 1,2,5,6,7,8,9 from tp7
    """

    def exercise1(self, coefficients, independent_terms):
        """
        Solves an equation system consisting of an upper diagonal matrix with ones in the diagonal.
        :param coefficients: upper diagonal nxn matrix
        :param independent_terms: nxn vector
        :return: nx1 X vector
        """
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

    def exercise2(self, coefficients, independent_terms):
        """
        Solves an equation system consisting of a lower diagonal matrix.
        :param coefficients: lower diagonal nxn matrix
        :param independent_terms: nxn vector
        :return: nx1 X vector
        """
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

    def exercise5WithoutPivoteo(self, coefficients, independent_terms):
        """
        Takes an equation system formed by a nxn coefficient matrix and an nx1 vector with independent terms. 
        Solves it using the gauss algorithm and returns the result.
        :param coefficients: nxn matrix
        :param independent_terms: nx1 vector
        :return: nx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        gauss_system(a, b)
        return self.exercise1(a, b)

    def exercise5PartialPivoteo(self, coefficients, independent_terms):
        """
        Takes an equation system formed by a nxn coefficient matrix and an nx1 vector with independent terms. 
        Solves it using the gauss algorithm with partial pivot and returns the result.
        :param coefficients: nxn matrix
        :param independent_terms: nx1 vector
        :return: nx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        gauss_system(a, b, partial_pivot)
        return self.exercise1(a, b)

    def exercise6(self, coefficients, independent_terms, calculator):
        """
        Takes an equation system formed by a nxn upper hessenberg coefficient matrix and an nx1 vector 
        with independent terms. Solves it using the gauss algorithm and returns the result.
        :param coefficients: nxn upper hessenberg matrix
        :param independent_terms: nx1 vector
        :return: nx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        gauss_upper_hessenberg(a, b, calculator)
        return self.exercise1(a, b)

    def exercise7(self, coefficients, independent_terms, calculator):
        """
        Takes an equation system formed by a nxm cubic spline coefficient matrix and an mx1 vector 
        with independent terms. Solves it using the gauss algorithm and returns the result.
        :param coefficients: nxn upper hessenberg matrix
        :param independent_terms: nx1 vector
        :return: nx1 X vector
        """
        a = copy.deepcopy(coefficients)
        b = copy.deepcopy(independent_terms)
        gauss_cubic_spline(a, b, calculator)
        return solve_cubic_spline_after_gauss(a, b, calculator)

    def exercise8(self, coefficients):
        """
        Calculates the inverse matrix of the received matrix using the Gauss-Jordan algorithm
        :param coefficients: nxn matrix
        :return: nxn matrix that is the calculated inverse
        """
        length = len(coefficients[0])
        for i in range(length):
            for j in range(length):
                if i == j:
                    coefficients[i].append(1)
                else:
                    coefficients[i].append(0)
        for k in range(length):
            first_value = coefficients[k][k]
            # fila paso 1.
            for j in range(k, length + 1 + k):
                coefficients[k][j] /= first_value
            #paso 2
            for i in range(length):
                if i != k:
                    first_row_value = coefficients[i][k]
                    for j in range(k, length + 1 + k):
                        coefficients[i][j] -= first_row_value * coefficients[k][j]
        inverse = []
        for i in range(length):
            inverse.append([])
            for j in range(length, length*2):
                inverse[i].append(coefficients[i][j])
        return inverse

    def exercise9(self, coefficients, independent_terms):
        """
        Takes an equation system formed by a nxn coefficient matrix and an nx1 vector with independent terms. 
        Solves it using LU decomposition and returns the result.
        :param coefficients: nxn matrix
        :param independent_terms: nx1 vector
        :return: nx1 X vector
        """
        length = len(coefficients)
        l = [[0 for _ in range(length)] for _ in range(length)]
        u = [[0 for _ in range(length)] for _ in range(length)]
        crout_decomposition(coefficients, l, u)
        z = self.exercise2(l, independent_terms)
        x = self.exercise1(u, z)
        return x



