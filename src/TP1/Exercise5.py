"""
    Takes an element and an array, returns true if the array contains the element, false if it doesn't.
"""


def contains_iterative(n, array):
    for i in range(0, len(array)):
        if array[i] == n:
            return True
    return False


def contains_recursive(n, array):
    return __aux_contains_(n, array, 0)


def __aux_contains_(n, array, current):
    if current >= len(array):
        return False
    elif array[current] == n:
        return True
    else:
        return __aux_contains_(n, array, current + 1)
