import unittest
from src.TP6.Calculator import Calculator
from src.TP6.Exercise1 import Exercise1


class TestEx1(unittest.TestCase):
    exc1 = Exercise1()
    calc = Calculator()

    def test_ex1a(self):
        matrix1 = [[1, 2], [2, 1]]
        self.assertEqual(2, self.exc1.exerciseA(matrix1, self.calc))

    def test_ex1b(self):
        matrix1 = [[1, 2], [2, 1]]
        self.assertEqual(4, self.exc1.exerciseB(matrix1, self.calc))

    def test_ex1c(self):
        matrix1 = [[1, 3, 2],
                   [5, 2, 1],
                   [3, 1, 3]]
        matrix3 = [[-8, -1, 3],
                   [-1, 7, 4],
                   [3, 4, 9]]
        self.assertEqual(6, self.exc1.exerciseC(matrix1, self.calc)[0])
        self.assertEqual(8, self.exc1.exerciseC(matrix1, self.calc)[1])
        self.assertEqual(7, self.exc1.exerciseC(matrix1, self.calc)[2])
        self.assertEqual(-6, self.exc1.exerciseC(matrix3, self.calc)[0])

    def test_ex1e(self):
        matrix2 = [[1, 1, 1],
                   [1, 2, 1],
                   [1, 1, 3]]
        matrix3 = [[-8, -1, 3],
                   [-1, 7, 4],
                   [3, 4, 9]]
        matrix23 = [[-7, 0, 4],
                    [0, 9, 5],
                    [4, 5, 12]]
        self.assertEqual(matrix23, self.exc1.exerciseE(matrix2, matrix3, self.calc))

if __name__ == '__main__':
    unittest.main()