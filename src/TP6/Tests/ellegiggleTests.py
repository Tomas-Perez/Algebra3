from src.TP6.Exercise1 import *

"""
1d)
"""
matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
vector = [1, 2, 3]
result = [1+8+21, 2+10+24, 3+12+27]
assert result == vector_matrix_product(matrix, vector)

"""
1f)
"""
matrixA = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
matrixB = [[2, 8, 2], [3, 2, 7], [1, 6, 4]]
result = [[24, 60, 96], [28, 64, 100], [25, 58, 91]]
assert result == matrix_product(matrixA, matrixB)
matrixA = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
matrixB = [[2, 3], [8, 2], [2, 7]]
result = [[48, 60], [60, 72], [72, 84]]
assert result == matrix_product(matrixA, matrixB)
