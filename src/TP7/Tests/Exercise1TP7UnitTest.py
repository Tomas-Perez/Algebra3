import unittest
from TP7.TP4 import *


class TestEx1(unittest.TestCase):
    exc1 = TP4()

    def test_ex1(self):
        matrix = [[1, 2],
                  [0, 1]]
        vector = [1, 2]
        result = [5, 2]
        x = self.exc1.exercise1(matrix, result)
        self.assertEqual(x, vector)

        matrix = [[1, 5, 8],
                  [0, 1, 3],
                  [0, 0, 1]]
        vector = [9, 8, 1]
        result = [57, 11, 1]
        x2 = self.exc1.exercise1(matrix, result)
        self.assertEqual(x2, vector)

if __name__ == '__main__':
    unittest.main()