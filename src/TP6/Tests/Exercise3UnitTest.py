import unittest
from src.TP6.Exercise3 import *
from src.TP6.Calculator import *


class TestEx3(unittest.TestCase):
    exc3 = Exercise3()
    calc = Calculator()

    def test_exc3ai(self):
        matrix = [[1, 2], [0, 4]]
        vector = [1, 2]
        result = [5, 8]
        self.assertEqual(self.exc3.exerciseAI(matrix, vector, self.calc), result)
        matrix = [[3, 5, 8], [0, 1, 3], [0, 0, 5]]
        vector = [9, 8, 1]
        result = [75, 11, 5]
        self.assertEqual(self.exc3.exerciseAI(matrix, vector, self.calc), result)

    def test_exc3aii(self):
        matrix1 = [[1, 2],
                   [0, 4]]
        matrix2 = [[3, 5],
                   [0, 6]]
        result = [[4, 7],
                  [0, 10]]
        self.assertEqual(self.exc3.exerciseAII(matrix1, matrix2, self.calc), result)

        matrix1 = [[5, 8, 6],
                   [0, 9, 3],
                   [0, 0, 1]]
        matrix2 = [[1, 1, 2],
                   [0, 7, 6],
                   [0, 0, 0]]
        result = [[6, 9, 8],
                  [0, 16, 9],
                  [0, 0, 1]]
        self.assertEqual(self.exc3.exerciseAII(matrix1, matrix2, self.calc), result)

    def test_exc3aiii(self):
        matrix1 = [[1, 2],
                   [0, 4]]
        matrix2 = [[3, 5],
                   [0, 6]]
        result = [[3, 17],
                  [0, 24]]
        self.assertEqual(self.exc3.exerciseAIII(matrix1, matrix2, self.calc), result)

        matrix1 = [[1, 2, 3],
                   [0, 5, 6],
                   [0, 0, 9]]
        matrix2 = [[1, 1, 2],
                   [0, 7, 6],
                   [0, 0, 0]]
        result = [[1, 15, 14],
                  [0, 35, 30],
                  [0, 0, 0]]
        self.assertEqual(self.exc3.exerciseAIII(matrix1, matrix2, self.calc), result)

        matrix1 = [[1.5, 3.2],
                   [0, 6]]
        matrix2 = [[3, 5],
                   [0, 6]]
        result = [[4.5, 26.700000000000003],
                  [0, 36]]
        self.assertEqual(self.exc3.exerciseAIII(matrix1, matrix2, self.calc), result)

if __name__ == '__main__':
    unittest.main()

