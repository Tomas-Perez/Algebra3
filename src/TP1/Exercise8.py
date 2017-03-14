"""
    Takes an array of the following form [a0, a1, ... an] representing a polynomial
    and a number for 'x'. Returns the value of the polynomial when evaluated with that 'x'.
"""


def horner(array, x):
    # counts the number of multiplications and sums for comparison
    amount_of_operations = 0
    s = array[0]
    for i in range(1, len(array)):
        s = s * x + array[i]
        # one sum and multiplication each time
        amount_of_operations += 2
    print("Amount of operations: ", amount_of_operations)
    return s


def horner_r(array, x):
    return horner_r_aux(array, x, 0, 0)


def horner_r_aux(array, x, i, s):
    if i == len(array):
        return s
    return horner_r_aux(array, x, i + 1, s * x + array[i])


def evaluate_polynomial(array, x):
    # counts the number of multiplications and sums for comparison
    amount_of_operations = 0
    result = 0
    for i in range(0, len(array)):
        result += array[0]*(x**i)
        # x**i counts as i multiplications, then we multiply by the n term and we sum it all
        amount_of_operations += i + 2
    print("Amount of operations: ", amount_of_operations)
    return result
