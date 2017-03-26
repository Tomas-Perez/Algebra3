"""
calculates the sum from 0 to n of i*x**i using summation
"""


def sum11(x, n):
    result = 0
    for i in range(0, n+1):
        result += i*(x**i)
    return result

"""
calculates the sum from 0 to n of i*x**i using the given formula
"""


def sum11_formula(x, n):
    result = n*(x**(n+2)) - (n+1)*(x**(n+1)) + x
    return result / ((x-1)**2)

