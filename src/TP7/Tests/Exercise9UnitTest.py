import unittest
from TP7.TP4 import *


class TP9Test(unittest.TestCase):
    tp4 = TP4()

    def test_decomposition(self):
        A = [[4, -2],
             [20, -7]]
        vector = [1, 2]
        result = [0, 6]
        L = [[0, 0],
             [0, 0]]
        U = [[0, 0],
             [0, 0]]

        doolittle_decomposition(A, L, U)

        print("Doolitle:")
        print("L:")
        print(L)

        print("U:")
        print(U)

        crout_decomposition(A, L, U)

        print("Crout:")
        print("L:")
        print(L)

        print("U:")
        print(U)

        # now the whole testing
        x_from_exc9 = self.tp4.exercise9(A, result)
        self.assertEqual(x_from_exc9, vector)


if __name__ == '__main__':
    unittest.main()
