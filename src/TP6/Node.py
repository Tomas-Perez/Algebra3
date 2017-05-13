class Node:

    def __init__(self, row, column, value):
        self.__row = row
        self.__column = column
        self.__value = value
    
    # This method should return the number of row, starting from 0.
    def getRow(self):
        return self.__row

    # This method should return the number of column, starting from 0.
    def getColumn(self):
        return self.__column

    # This method should return the number contained inside the node.
    def getValue(self):
        return self.__value

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

