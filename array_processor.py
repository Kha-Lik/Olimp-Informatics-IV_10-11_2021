from array import *


def process(array):
    sum = 0
    i = 0
    for row in array:
        j = 0
        for cell in row:
            if cell >= 0 and cell % 2 == 0:
                sum += cell**2

            if cell >= 0:
                array[i][j] = 1
            else:
                array[i][j] = 0

            j += 1
        i += 1

    return sum
