import unittest
from TP6.Exercise4 import *
from TP6.Calculator import Calculator


class TestEx4(unittest.TestCase):
    exc4 = Exercise4()
    calc = Calculator()

    def test_matrix_to_node_array(self):
        expected = [Node(0, 0, 1), Node(0, 1, 2), Node(0, 2, 3), Node(1, 1, 4), Node(1, 2, 5), Node(2, 2, 6)]
        matrix = [[1, 2, 3],
                  [0, 4, 5],
                  [0, 0, 6]]
        actual = self.exc4.matrix_to_node_array(matrix)
        self.assertEqual(expected, actual)

    def test_summation(self):
        matrix1 = [[1, 2, 3],
                   [0, 4, 5],
                   [0, 0, 6]]
        matrix2 = [[4, 0, 8],
                   [0, 6, 1],
                   [0, 0, 7]]
        expected = [[5, 2, 11],
                    [0, 10, 6],
                    [0, 0, 13]]
        linear_matrix1 = self.exc4.matrix_to_node_array(matrix1)
        linear_matrix2 = self.exc4.matrix_to_node_array(matrix2)
        linear_expected = self.exc4.matrix_to_node_array(expected)
        actual_sum = self.exc4.summation(linear_matrix1, linear_matrix2, self.calc)
        self.assertEqual(linear_expected, actual_sum)

if __name__ == '__main__':
    unittest.main()
