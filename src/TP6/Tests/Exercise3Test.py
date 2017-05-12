from TP6.Exercise3 import *


def exc3ai_test():
    matrix = [[1, 0], [2, 4]]
    vector = [1, 2]
    result = [5, 8]
    assert exc3ai(matrix, vector) == result
    matrix = [[3, 0, 0], [5, 1, 0], [8, 3, 5]]
    vector = [9, 8, 1]
    result = [75, 11, 5]
    assert exc3ai(matrix, vector) == result


def exc3aii_test():
    matrix1 = [[1, 0], [2, 4]]
    matrix2 = [[3, 0], [5, 6]]
    result = [[4, 0], [7, 10]]
    assert exc3aii(matrix1, matrix2) == result

    matrix1 = [[5, 0, 0], [8, 9, 0], [6, 3, 1]]
    matrix2 = [[1, 0, 0], [4, 7, 0], [2, 6, 0]]
    result = [[6, 0, 0], [12, 16, 0], [8, 9, 1]]
    assert exc3aii(matrix1, matrix2) == result


def exc3aiii_test():
    matrix1 = [[1, 0], [2, 4]]
    matrix2 = [[3, 0], [5, 6]]
    result = [[3, 0], [17, 24]]
    assert exc3aiii(matrix1, matrix2) == result

exc3ai_test()
exc3aii_test()
exc3aiii_test()

