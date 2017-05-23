import unittest
from TP7.TP4 import *


class TestEx2(unittest.TestCase):
    exc2 = TP4()

    def test_ex2(self):
        matrix = [[5, 0],
                  [2, 3]]
        vector = [1, 2]
        result = [5, 8]
        x = self.exc2.exercise2(matrix, result)
        self.assertEqual(x, vector)

        matrix = [[5, 0, 0],
                  [5, 3, 0],
                  [8, 3, 2]]
        vector = [9, 8, 1]
        result = [45, 69, 98]
        x2 = self.exc2.exercise2(matrix, result)
        self.assertEqual(x2, vector)

if __name__ == '__main__':
    unittest.main()
