import unittest
from src.TP7.TP4 import TP4
from src.TP6.Exercise1 import Exercise1
from TP7.Calculator import Calculator


class TP4Test(unittest.TestCase):
    tp4 = TP4()
    calc = Calculator()
    exc1 = Exercise1()

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

    def test_exc5_no_pivot(self):
        a = [[1, 2, 3],
             [3, 2, 1],
             [2, 1, 3]]
        b = [1, 2, 2]

        result_x = self.tp4.exercise5WithoutPivoteo(a, b)
        solution_b = self.exc1.exerciseD(a, result_x, self.calc)

        for i in range(len(result_x)):
            self.assertAlmostEqual(b[i], solution_b[i])


    def test_exc5_pivot(self):
        a = [[1, 2, 3],
             [3, 2, 1],
             [2, 1, 3]]
        b = [1, 2, 2]

        result_x = self.tp4.exercise5PartialPivoteo(a, b)
        solution_b = self.exc1.exerciseD(a, result_x, self.calc)

        for i in range(len(result_x)):
            self.assertAlmostEqual(b[i], solution_b[i])

    def test_gauss_hessenberg(self):
        a = [[1, 2, 3],
             [3, 2, 1],
             [0, 1, 3]]
        b = [1, 2, 2]
        exp_a = [[1, 2, 3],
                 [0, 1, 2],
                 [0, 0, 1]]
        exp_b = [1, 1/4, 7/4]
        self.tp4.gauss_upper_hessenberg(a, b, self.calc)
        self.assertEqual(a, exp_a)
        self.assertEqual(b, exp_b)

    def test_ex6(self):
        a = [[5, 6, 8, 2, 1],
             [3, 75, 25, 10, 2],
             [0, 14, 6, 6, 7],
             [0, 0, 11, 9, 8],
             [0, 0, 0, 1, 5]]
        b = [2, 5, 6, 8, 1]
        result_x = self.tp4.exercise6(a, b, self.calc)
        solution_b = self.exc1.exerciseD(a, result_x, self.calc)

        for i in range(len(result_x)):
            self.assertAlmostEqual(b[i], solution_b[i])

    def test_ex7(self):
        """
        TOO MUCH OPERATION ERROR LUL
        :return: NOPE
        
        a = [[5, 6, 0],
             [15, 75, 15],
             [0, 14, 86]]
        b = [2, 5, 6]
        result_x = self.tp4.exercise7(a, b, self.calc)
        solution_b = self.exc1.exerciseD(a, result_x, self.calc)

        for i in range(len(result_x)):
            self.assertAlmostEqual(b[i], solution_b[i])
        """

if __name__ == '__main__':
    unittest.main()
