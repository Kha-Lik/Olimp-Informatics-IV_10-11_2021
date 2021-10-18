import sum_of_digits
import calculate_function
import sum_of_fractions

print("==First task==")
print("Enter three-digit number:")
num = int(input())

print(sum_of_digits.calculate_three_digit(num))

print("==Second task==")
print("Enter x and y separating with space:")
(x, y) = input().split()

print(calculate_function.calculate(float(x), float(y)))

print("==Third task==")
print("Enter x and number of additions separating with space:")
(x, n) = input().split()

print(sum_of_fractions.calculate(float(x), int(n)))
