import unittest
from TP7.TP4 import *
from TP7.Calculator import *


class TestEx4(unittest.TestCase):
    tp4 = TP4()
    calc = Calculator()

    def test_exercise8(self):
        matrix = [[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]]
        inverse = [[4.0, 3.0, -1.0],
                   [-2.0, -2.0, 1.0],
                   [5.0, 4.0, -1.0]]

        self.assertEqual(self.tp4.exercise8(matrix), inverse)

if __name__ == '__main__':
    unittest.main()
