"""
calculates the sum from m to n, of the sum from r to s, of j*k
"""


def sum9(m, n, r, s, j, k):
    result = 0
    for i in range(m, n+1):
        for s in range(r, s+1):
            result += j*k
    return result

