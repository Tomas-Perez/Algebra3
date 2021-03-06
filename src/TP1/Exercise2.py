# a
"""
calculates the factorial of n in an iterative and recursive way
"""


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    return __aux_factorial(1, n)


def __aux_factorial(current, n):
    if n <= 1:
        return current
    else:
        return __aux_factorial(current * n, n-1)


# b
"""
calculates 2**n
"""


def two_to_the_n(n):
    return 2**n


def two_to_the_n_recursive(n):
    if n == 0:
        return 1
    else:
        return 2 * two_to_the_n_recursive(n - 1)


# c
"""
calculates the Nth term of the Fibonacci sequence in an iterative and recursive way
"""


def fibonacci_iterative(n):
    result = 0
    current_num = 0
    next_num = 1
    for i in range(1, n+1):
        result = current_num
        temp = current_num
        current_num = next_num
        next_num += temp
    return result

"""
calculates the Nth term of the Fibonacci sequence in an iterative and recursive way
"""


def fibonacci_recursive(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# d
"""
calculates the greatest common divisor between two numbers in an iterative and recursive way
"""


def gcd_iterative(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a%b)