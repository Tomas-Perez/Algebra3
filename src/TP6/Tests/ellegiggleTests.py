from src.TP6.Exercise1 import *

"""
1d)
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
vector = [1,2,3]
result = [1+8+21,2+10+24,3+12+27]
assert result == vector_matrix_product(matrix,vector)

"""
1f)
"""
matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = [[2,3,1],[8,2,6],[2,7,4]]
result = [[24,28,25],[60,64,58],[96,100,91]]
assert result == matrix_product(matrixA,matrixB)
matrixA = [[1,2,3],[4,5,6],[7,8,9]]
matrixB = [[2,3],[8,2],[2,7]]
result = [[24,28],[60,64],[96,100]]
assert result == matrix_product(matrixA,matrixB)