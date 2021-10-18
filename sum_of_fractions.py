def calculate(x, n):
    sum = 0
    multiplier = 1

    for i in range(1, n*2, 2):
        sum += multiplier*(x**i/i)
        multiplier *= -1

    return sum
