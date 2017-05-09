from src.TP6.Exercise1 import *

matrix1 = [[1, 2], [2, 1]]
matrix2 = [[-1, -2], [-2, -1]]

#assert 2 == diag_sum(matrix1)
#assert 4 == secondary_diag_sum(matrix1)

"""
1c)
"""
assert ex1c(matrix1)[0] == 3


"""
1e)
"""
assert ex1e(matrix1, matrix2)[0][0] == 0
