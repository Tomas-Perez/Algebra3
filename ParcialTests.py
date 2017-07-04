import unittest
from ParcialAlgebra3 import *


class ParcialTest(unittest.TestCase):

    def test_upside_down_gauss(self):
        a = [[1, 2],
             [3, 4]]
        b = [4, 2]
        upside_down_gauss(a, b)

        a = [[2, 1, 3],
             [6, 3, 7],
             [1, 2, 6]]
        b = [6, 7, 8]
        upside_down_gauss(a, b)

    def test_tridiag_symm(self):
        test_matrix = [[7, 2, 0],
                       [2, 5, 3],
                       [0, 3, 3]]

        test_matrix_wrong = [[7, 2, 0],
                             [2, 5, 4],
                             [0, 3, 3]]
        self.assertTrue(is_tridiagonal_symmetric(test_matrix))
        self.assertFalse(is_tridiagonal_symmetric(test_matrix_wrong))

    def test_solve_with_gauss(self):
        a = [[1, 2],
             [3, 4]]
        b = [4, 2]
        exp_result = [-6, 5]
        actual_result = solve_with_upside_down_gauss(a, b)
        print(b)
        print(actual_result)
        for i in range(len(b)):
            self.assertAlmostEqual(exp_result[i], actual_result[i])
        a = [[2, 1, 3],
             [6, 3, 7],
             [1, 2, 6]]
        b = [6, 7, 8]
        exp_result = [4/3, -79/6, 11/2]
        actual_result = solve_with_upside_down_gauss(a, b)
        for i in range(len(b)):
            self.assertAlmostEqual(exp_result[i], actual_result[i])

            
if __name__ == '__main__':
    unittest.main()
