def how_many_zeros_iterative(n):
    num_of_zeros = 0
    while n > 9:
        if (n % 10) == 0:
            num_of_zeros += 1
        n /= 10
        n = int(n)
    return num_of_zeros


def how_many_zeros_recursive(n):
    return __aux_how_many_zeros(0, n)


def __aux_how_many_zeros(count, n):
    if n <= 9:
        return count
    elif n % 10 == 0:
        return __aux_how_many_zeros(count+1, int(n/10))
    else: return __aux_how_many_zeros(count, int(n/10))
