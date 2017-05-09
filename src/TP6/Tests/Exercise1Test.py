from src.TP6.Exercise1 import *

def exc1_a_test():matrix1 = [[1,2],[2,1]]

matrix2 = [[-1, -2], [-2, -1]]

#assert 2 == diag_sum(matrix1)def exc1_b_test():
    matrix1 = [[1, 2], [2, 1]]
#assert 4 == secondary_diag_sum(matrix1)"""
1c)
"""
assert ex1c(matrix1)[0] == 3


"""
1e)
"""
assert ex1e(matrix1, matrix2)[0][0] == 0


def exc1_c_test():
    matrix = [[1, 2], [3, 4], [5, 6]]
    matrix_t = transpose_matrix(matrix)
    assert matrix_t == [[1, 3, 5], [2, 4, 6]]

exc1_a_test()
exc1_b_test()
exc1_c_test()