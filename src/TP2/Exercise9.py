"""
calculates the sum of j*k such that (m <= j <= n) and (r <= k <= s), using summation.
"""


def sum9(m, n, r, s):
    result = 0
    for j in range(m, n+1):
        for k in range(r, s+1):
            result += j*k
    return result

"""
calculates the sum of j*k such that (m <= j <= n) and (r <= k <= s), using the formula we cleared from the summation.
"""


def sum9_formula(m, n, r, s):
    result = (n-m+1)*(s-r+1)*(s+r)*(n+m)
    return result/4

