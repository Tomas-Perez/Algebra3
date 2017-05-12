import unittest
from TP6.Exercise3 import *


class TestEx3(unittest.TestCase):

    def test_exc3ai(self):
        matrix = [[1, 2], [0, 4]]
        vector = [1, 2]
        result = [5, 8]
        self.assertEqual(exc3ai(matrix, vector), result)
        matrix = [[3, 5, 8], [0, 1, 3], [0, 0, 5]]
        vector = [9, 8, 1]
        result = [75, 11, 5]
        self.assertEqual(exc3ai(matrix, vector), result)

    def test_exc3aii(self):
        matrix1 = [[1, 2],
                   [0, 4]]
        matrix2 = [[3, 5],
                   [0, 6]]
        result = [[4, 7],
                  [0, 10]]
        self.assertEqual(exc3aii(matrix1, matrix2), result)

        matrix1 = [[5, 8, 6],
                   [0, 9, 3],
                   [0, 0, 1]]
        matrix2 = [[1, 1, 2],
                   [0, 7, 6],
                   [0, 0, 0]]
        result = [[6, 9, 8],
                  [0, 16, 9],
                  [0, 0, 1]]
        self.assertEqual(exc3aii(matrix1, matrix2), result)

    def test_exc3aiii(self):
        matrix1 = [[1, 2],
                   [0, 4]]
        matrix2 = [[3, 5],
                   [0, 6]]
        result = [[3, 17],
                  [0, 24]]
        self.assertEqual(exc3aiii(matrix1, matrix2), result)

        matrix1 = [[1, 2, 3],
                   [0, 5, 6],
                   [0, 0, 9]]
        matrix2 = [[1, 1, 2],
                   [0, 7, 6],
                   [0, 0, 0]]
        result = [[1, 15, 14],
                  [0, 35, 30],
                  [0, 0, 0]]
        self.assertEqual(exc3aiii(matrix1, matrix2), result)

if __name__ == '__main__':
    unittest.main()

