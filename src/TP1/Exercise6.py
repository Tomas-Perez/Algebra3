from math import sqrt


# b1
def is_prime_iterative(n):
    for i in range(int(sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True


def is_prime_recursive(n):
    return __aux_is_prime(n,2)


def __aux_is_prime(n, current):
    if current > sqrt(n):
        return True
    elif n % current == 0:
        return False
    else:
        return __aux_is_prime(n, current+1)


# b2
def next_prime_iterative(n):
    i = n
    while not is_prime_iterative(i):
        i += 1
    return i


def next_prime_recursive(n):
    if not is_prime_iterative(n):
        return next_prime_recursive(n + 1)
    else:
        return n


# b3
def how_many_factors_iterative(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0 and is_prime_iterative(i):
            n /= i
            count += 1
    return count


def how_many_factors_recursive(n):
    return __aux_how_many_factors(n, 1, 0)


def __aux_how_many_factors(n, current, count):
    if current > n:
        return count
    elif n % current == 0 and is_prime_iterative(current):
        return __aux_how_many_factors(n/current, current + 1, count + 1)
    else:
        return __aux_how_many_factors(n, current + 1, count)


# b4
def prime_factors_iterative(n):
    array = []
    for i in range(1, n + 1):
        if n % i == 0 and is_prime_iterative(i):
            n /= i
            array.append(i)
    return array


def prime_factors_recursive(n):
    return __aux_prime_factors(n, 1, [])


def __aux_prime_factors(n, current, array):
    if current > n:
        return array
    elif n % current == 0 and is_prime_iterative(current):
        array.append(current)
        return __aux_prime_factors(n / current, current + 1, array)
    else:
        return __aux_prime_factors(n, current + 1, array)
