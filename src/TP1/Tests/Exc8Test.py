from src.TP1.Exercise8 import *
print("Horner [10,5,8,1] x = 3: {}" .format(horner([10, 5, 8, 1], 3)))
print("Recursive Horner [10,5,8,1] x = 3: {}" .format(horner_r([10, 5, 8, 1], 3)))
print("Regular evaluation [10,5,8,1] x = 3: {}" .format(evaluate_polynomial([10, 5, 8, 1], 3)))