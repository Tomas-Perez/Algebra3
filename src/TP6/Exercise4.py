from TP6.Node import Node


class Exercise4:

    """
    Contains algorithms to solve exercise 4
    """

    """
    Takes two matrices stored in a Node[] and returns their sum
    """
    def summation(self, matrixA, matrixB, calculator):
        result = []
        matrix_size = len(matrixA)
        for x in range(matrix_size):
            node_value = calculator.sum(matrixA[x].getValue(), matrixB[x].getValue())
            result.append(Node(matrixA[x].getRow(), matrixA[x].getColumn(), node_value))
        return result

    """
    Takes a matrix and returns it as a linear list of nodes
    """
    def matrix_to_node_array(self, matrix):
        node_array = []
        matrix_size = len(matrix)
        for n in range(matrix_size):
            for m in range(n, matrix_size):
                node_array.append(Node(n, m, matrix[n][m]))
        return node_array
