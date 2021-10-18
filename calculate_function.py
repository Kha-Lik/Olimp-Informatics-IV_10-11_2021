from math import sqrt, sin, cos


def calculate(x, y):
    first_part = (x**3)/(3*y)
    third_part = 3*sin(y)/cos(x/y)

    num = x**3-8*x
    if num < 0:
        print("Error: cannot get sqrt of negative number")
        return
    second_part = sqrt(num)

    return first_part + second_part + third_part
