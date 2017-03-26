"""
    Receives an array and returns true if it's a palindrome, false if it isn't
"""


def is_palindrome_iterative(array):
    begin = 0
    end = len(array) - 1
    while begin < end:
        if array[begin] != array[end]:
            return False
        begin += 1
        end -= 1
    return True


def is_palindrome_recursive(array):
    return __aux_is_palindrome(0, len(array) - 1, array)


def __aux_is_palindrome(begin, end, array):
    if begin > end:
        return True
    elif array[begin] != array[end]:
        return False
    else:
        return __aux_is_palindrome(begin + 1, end - 1, array)

