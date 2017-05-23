import unittest
from TP7.TP4 import *
from TP7.Calculator import *

class TestEx4(unittest.TestCase):
    tp4 = TP4()
    calc = Calculator()

    def exercise8(self):

        self.tp4.exercise8()

if __name__ == '__main__':
    unittest.main()
