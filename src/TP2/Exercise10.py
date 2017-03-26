"""
calculates the sum from 1 to n of i*2**i using summation
"""


def sum10(n):
    result = 0
    for i in range(1, n+1):
        result += i*(2**i)
    return result

"""
calculates the sum from 1 to n of i*2**i using the formula we cleared from the summation
"""


def sum10_formula(n):
    return 2*(n*(2**n)-2**n+1)
