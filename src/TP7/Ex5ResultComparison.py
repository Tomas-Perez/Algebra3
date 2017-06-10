from random import randint
from src.TP6.Exercise1 import Exercise1
from TP7.Calculator import Calculator
from src.TP7.TP4 import TP4


def get_better_approx(a, b, function_1, function_2):
    exc1 = Exercise1()
    function_1_result = function_1(a,b)
    function_2_result = function_2(a,b)
    function_1_b = exc1.exerciseD(a, function_1_result, Calculator())
    function_2_b = exc1.exerciseD(a, function_2_result, Calculator())
    total_delta_1 = 0
    total_delta_2 = 0
    for i in range(len(b)):
        total_delta_1 += abs(b[i] - function_1_b[i])
        total_delta_2 += abs(b[i] - function_2_b[i])

    if total_delta_1 < total_delta_2:
        return 1
    elif total_delta_2 < total_delta_1:
        return 2
    else:
        return 0


if __name__ == '__main__':
    length = 3
    tp4 = TP4()
    count_pivot = 0
    count_no_pivot = 0
    count_even = 0
    for _ in range(20):
        a = [[randint(1, 50) for _ in range(length)] for _ in range(length)]
        b = [randint(1, 50) for _ in range(length)]
        better_approx = get_better_approx(a, b, tp4.exercise5WithoutPivoteo, tp4.exercise5PartialPivoteo)
        if better_approx == 1:
            count_no_pivot += 1
        elif better_approx == 2:
            count_pivot += 1
        else:
            count_even += 1
    print("Pivot was better %d times" % count_pivot)
    print("Pivot was worse %d times" % count_no_pivot)
    print("They were even %d times" % count_even)