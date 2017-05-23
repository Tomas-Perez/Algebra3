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

    def test_exc3Bi(self):
        matrix = [[5, 4, 0],
                  [3, 9, 7],
                  [0, 5, 1]]
        vector = [1, 2, 3]
        result = [13, 42, 13]
        self.assertEqual(self.exc3.exerciseBI(matrix, vector, self.calc), result)

        matrix = [[5, 4, 0, 0],
                  [3, 9, 7, 0],
                  [0, 5, 1, 6],
                  [0, 0, 6, 9]]
        vector = [1, 2, 3, 4]
        result = [13, 42, 37, 54]
        self.assertEqual(self.exc3.exerciseBI(matrix, vector, self.calc), result)

    def test_exc3Bii(self):
        matrix1 = [[1, 4, 0],
                   [2, 5, 8],
                   [0, 6, 9]]
        matrix2 = [[2, 8, 2],
                   [3, 2, 7],
                   [1, 6, 4]]
        result = [[3, 12, 2],
                  [5, 7, 15],
                  [1, 12, 13]]
        self.assertEqual(self.exc3.exerciseBII(matrix1, matrix2, self.calc), result)

    def test_exc3Biii(self):
        matrix1 = [[1, 4, 0],
                   [2, 5, 8],
                   [0, 6, 9]]
        matrix2 = [[2, 3],
                   [8, 2],
                   [2, 7]]
        result = [[34, 11],
                  [60, 72],
                  [66, 75]]
        self.assertEqual(self.exc3.exerciseBIII(matrix1, matrix2, self.calc), result)

        matrix1 = [[3, 0, 0, 0],
                   [4, 5, 0, 0],
                   [8, 9, 7, 0],
                   [0, 3, 4, 8]]

        matrix2 = [[1, 5],
                   [7, 5],
                   [4, 12],
                   [4, 6]]

        result = [[3, 15],
                  [39, 45],
                  [99, 169],
                  [69, 111]]
        self.assertEqual(self.exc3.exerciseBIII(matrix1, matrix2, self.calc), result)

    def test_exc3Dii(self):
        matrix1 = [[1, 4, 0],
                   [2, 5, 8],
                   [0, 6, 9]]
        matrix2 = [[2, 8, 2],
                   [3, 2, 7],
                   [1, 6, 4]]
        result = [[3, 12, 2],
                  [5, 7, 15],
                  [1, 12, 13]]
        self.assertEqual(self.exc3.exerciseDII(matrix1, matrix2, 1, 1, self.calc), result)

    def test_exc3Diii(self):
        matrix1 = [[1, 4, 0],
                   [2, 5, 8],
                   [0, 6, 9]]
        matrix2 = [[2, 3],
                   [8, 2],
                   [2, 7]]
        result = [[34, 11],
                  [60, 72],
                  [66, 75]]
        self.assertEqual(self.exc3.exerciseDIII(matrix1, matrix2, 1, 1, self.calc), result)

        matrix1 = [[3, 0, 0, 0],
                   [4, 5, 0, 0],
                   [8, 9, 7, 0],
                   [0, 3, 4, 8]]

        matrix2 = [[1, 5],
                   [7, 5],
                   [4, 12],
                   [4, 6]]

        result = [[3, 15],
                  [39, 45],
                  [99, 169],
                  [69, 111]]
        self.assertEqual(self.exc3.exerciseDIII(matrix1, matrix2, 2, 0, self.calc), result)

    def test_exc3E(self):
        matrix1 = [[5, 0, 0],
                   [3, 9, 0],
                   [1, 5, 1]]
        matrix2 = [[1, 1, 2],
                   [0, 7, 6],
                   [0, 0, 4]]
        result = [[5, 5, 10],
                  [3, 66, 60],
                  [1, 36, 36]]
        self.assertEqual(self.exc3.exerciseE(matrix1, matrix2, self.calc), result)

    def test_exc3ci(self):
        matrix = [[5, 4, 0],
                  [3, 9, 7],
                  [0, 5, 1]]
        vector = [1, 2, 3]
        result = [13, 42, 13]
        self.assertEqual(self.exc3.exerciseCI(matrix, vector, self.calc), result)

        matrix = [[5, 4, 0, 0],
                  [3, 9, 7, 0],
                  [0, 5, 1, 6],
                  [0, 0, 6, 9]]
        vector = [1, 2, 3, 4]
        result = [13, 42, 37, 54]
        self.assertEqual(self.exc3.exerciseCI(matrix, vector, self.calc), result)

    def test_exc3cii(self):
        matrix1 = [[5, 4, 0],
                   [3, 9, 7],
                   [0, 5, 1]]
        matrix2 = [[5, 4, 0],
                   [3, 9, 7],
                   [0, 5, 1]]
        result = [[10, 8, 0],
                  [6, 18, 14],
                  [0, 10, 2]]
        self.assertEqual(self.exc3.exerciseCII(matrix1, matrix2, self.calc), result)

        matrix1 = [[5, 4, 0, 0],
                   [3, 9, 7, 0],
                   [0, 5, 1, 6],
                   [0, 0, 6, 9]]
        matrix2 = [[5, 4, 0, 0],
                   [3, 9, 7, 0],
                   [0, 5, 1, 6],
                   [0, 0, 6, 9]]
        result = [[10, 8, 0, 0],
                  [6, 18, 14, 0],
                  [0, 10, 2, 12],
                  [0, 0, 12, 18]]
        self.assertEqual(self.exc3.exerciseCII(matrix1, matrix2, self.calc), result)

    def test_exc3ciii(self):
        matrix1 = [[5, 4, 0],
                   [3, 9, 7],
                   [0, 5, 1]]
        matrix2 = [[7, 4, 0],
                   [3, 2, 47],
                   [0, 5, 10]]
        result = [[47, 28, 188],
                  [48, 65, 493],
                  [15, 15, 245]]
        self.assertEqual(self.exc3.exerciseCIII(matrix1, matrix2, self.calc), result)


if __name__ == '__main__':
    unittest.main()
