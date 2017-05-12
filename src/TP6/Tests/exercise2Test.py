from src.TP6.Exercise2 import *

"""
test exercise 2
"""

matrix1 = [[1, 3, 2], [2, 2, 1], [3, 1, 3]]
matrix2 = [[1, 1, 1], [1, 2, 1], [1, 1, 3]]
dominant_matrix = [[6, 2, 1], [-1, 8, 2], [1, 1, 6]]

"""
2a)
"""
assert is_symmetrical(matrix2)
assert not is_symmetrical(matrix1)


"""
2b)
"""
assert is_dominant(dominant_matrix)
assert not is_dominant(matrix1)