
"""
calculates the sum of 1+ 2 + 3 + 4 + ... + n in iterative and recursive way
"""
# a


def sum_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += i
    return result


def sum_recursive(n):
    return __aux_sum(0, n)


def __aux_sum(current, n):
    if n <= 0:
        return current
    else:
        return __aux_sum(current + n, n-1)


# b
"""
calculates the sum of 1**2 + 2**2 + 3**2 + ... + n**2 in an iterative and recursive way
"""


def square_sum_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += i**2
    return result


def square_sum_recursive(n):
    return __aux_square_sum(0, n)


def __aux_square_sum(current, n):
    if n <= 0:
        return current
    else:
        return __aux_square_sum(current + n**2, n-1)


# c
"""
calculates the sum of p**0 + p**1 + p**2 + ... + p**n in an iterative and recursive way
"""


def p_sum_iterative(p, n):
    result = 0
    for i in range(0, n+1):
        result += p**i
    return result


def p_sum_recursive(p, n):
    return __aux_p_to_the_n(0, p, n)


def __aux_p_to_the_n(current, p, n):
    if n <= -1:
        return current
    else:
        return __aux_p_to_the_n(current + p**n, p, n-1)


# d
"""
calculates the sum of p**0 + p**1 + p**2 + ... + p**n in an iterative and recursive way
"""
def odd_num_sum_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += 2*i - 1
    return result


def odd_num_sum_recursive(n):
    return __aux_odd_num_sum(0, n)


def __aux_odd_num_sum(current, n):
    if n <= 0:
        return current
    else:
        return __aux_odd_num_sum(current + 2*n - 1, n-1)


# e
def n_times_n_plus_one_sum_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += i * (i+1)
    return result


def n_times_n_plus_one_sum_recursive(n):
    return __aux_n_times_n_plus_one(0, n)


def __aux_n_times_n_plus_one(current, n):
    if n <= 0:
        return current
    else:
        return __aux_n_times_n_plus_one(current + n * (n+1), n-1)


# f
def cube_num_sum_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += i**3
    return result


def cube_num_sum_recursive(n):
    return __aux_cube_sum(0, n)


def __aux_cube_sum(current, n):
    if n <= 0:
        return current
    else:
        return __aux_cube_sum(current + n**3, n-1)
