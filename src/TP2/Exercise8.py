"""
calculates the sum of j, from m to n
"""


def sum8(m, n, j):
    result = 0
    for j in range(m, n+1):
        result += j
    return result