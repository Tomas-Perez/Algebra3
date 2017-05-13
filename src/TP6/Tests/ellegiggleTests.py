from src.TP6.Exercise1 import *
from src.TP6.Calculator import *

calculator = Calculator()
ex1 = Exercise1()


"""
1d)
"""
matrix = [[1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]]
vector = [1,
          2,
          3]
result = [1+8+21,
          2+10+24,
          3+12+27]
assert result == ex1.exerciseD(matrix, vector, calculator)

"""
1f)
"""
matrixA = [[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]]
matrixB = [[2, 8, 2],
           [3, 2, 7],
           [1, 6, 4]]
result = [[21, 58, 58],
          [27, 74, 71],
          [33, 90, 84]]
assert result == ex1.exerciseF(matrixA, matrixB, calculator)

matrixA = [[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]]
matrixB = [[2, 3],
           [8, 2],
           [2, 7]]
result = [[48, 60],
          [60, 72],
          [72, 84]]
assert result == ex1.exerciseF(matrixA, matrixB, calculator)

matrixA = [[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]]
matrixB = [[2, 3],
           [8, 2]]
result = None

assert result == None


