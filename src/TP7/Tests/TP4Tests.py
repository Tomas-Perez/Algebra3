import unittest
from src.TP7.TP4 import TP4
from TP7.Calculator import Calculator


class TP4Test(unittest.TestCase):
    tp4 = TP4()
    calc = Calculator()

    def test_gauss_system(self):
        a = [[1, 2, 3],
             [3, 2, 1],
             [2, 1, 3]]
        b = [1, 2, 2]
        exp_a = [[1, 2, 3],
                 [0, 1, 2],
                 [0, 0, 1]]
        exp_b = [1, 0.25, 0.25]
        self.tp4.gauss_system(a, b)
        self.assertEqual(a, exp_a)
        self.assertEqual(b, exp_b)

        a = [[1, 2, 3],
             [3, 2, 1],
             [2, 1, 3]]
        b = [1, 2, 2]
        exp_a = [[1, 2/3, 1/3],
                 [0, 1, 2],
                 [0, 0, 1]]
        exp_b = [2/3, 1/4, 1/4]
        self.tp4.gauss_system(a, b, self.tp4.partial_pivot)
        for i in range(len(a)):
            self.assertAlmostEqual(b[i], exp_b[i])
            for j in range(len(a)):
                self.assertAlmostEqual(a[i][j], exp_a[i][j])



if __name__ == '__main__':
    unittest.main()
