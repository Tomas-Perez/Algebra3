"""
calculates the sum of the integers from m to n using summation
"""


def sum8(m, n):
    result = 0
    for j in range(m, n+1):
        result += j
    return result

"""
calculates the sum of the integers from m to n, using the formula we cleared from the summation
"""


def sum8_formula(m, n):
    result = (n-m+1)*(n+m)
    return result/2
