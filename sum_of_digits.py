import math


def calculate_three_digit(number):
    if number in range(100, 1000) or number in range(-999, -99):
        sum = 0
        for i in [2, 1, 0]:
            sum += int(number/10**i)
            number = math.fmod(number, 10**i)

        return sum

    print("Invalid number. Must be a three-digit integer")
