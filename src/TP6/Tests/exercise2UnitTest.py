import unittest
from src.TP6.Exercise2 import *
from src.TP6.Calculator import *


class TestEx2(unittest.TestCase):
    exc2 = Exercise2()
    calc = Calculator()

    def test_ex2a(self, exc2=Exercise2(), calc=Calculator()):
        matrix1 = [[1, 3, 2],  # not symmetrical
                   [5, 2, 1],
                   [3, 1, 3]]
        matrix2 = [[1, 1, 1],  # symmetrical
                   [1, 2, 1],
                   [1, 1, 3]]
        matrix3 = [[-8, -1, 3],  # symmetrical
                   [-1, 7, 4],
                   [3, 4, 9]]

        self.assertTrue(self, exc2.exerciseA(matrix2, calc))
        self.assertTrue(self, not exc2.exerciseA(matrix1, calc))
        self.assertTrue(self, exc2.exerciseA(matrix3, calc))

    def test_ex2b(self, exc2=Exercise2(), calc=Calculator()):
        dominant_matrix = [[6, 2, 1],
                           [-1, 8, 2],
                           [1, 1, 6]]
        matrix1 = [[1, 3, 2],  # not dominant
                   [2, 2, 1],
                   [3, 1, 3]]

        self.assertTrue(self, exc2.exerciseB(dominant_matrix, calc))
        self.assertTrue(self, not exc2.exerciseB(matrix1, calc))

if __name__ == '__main__':
    unittest.main()
