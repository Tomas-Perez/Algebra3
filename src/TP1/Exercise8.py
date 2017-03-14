def horner(array, x):
    s = array[0]
    for i in range(1, len(array)):
        s = s * x + array[i]
    return s


def horner_r(array, x):
    return Horner_r_aux(array, x, 0, 0) 


def horner_r_aux(array, x, i, s):
    if(i == len(array)):
        return s
    return Horner_r_aux(array, x, i + 1, s * x + array[i])
