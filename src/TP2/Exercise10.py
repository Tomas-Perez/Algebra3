"""
calculates the sum from 1 to n of i*2**i
"""


def sum10(n):
    result = 0
    for i in range(1, n+1):
        result += i*2**i
    return result

