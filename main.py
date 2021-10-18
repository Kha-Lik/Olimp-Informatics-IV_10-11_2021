import sum_of_digits
import calculate_function
import sum_of_fractions
import array_processor

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

print("==Fourth task==\n")
array = [[22, 215, 0, -4, 28, 125],
         [87, 44, -22, 7, 123, -39],
         [-9, -5, 0, 63, -17, 45],
         [22, -3, -4, -8, 9, -122],
         [-21, -8, -5, 45, 32, 77]]

print("Initial array:")
print('\n'.join(' '.join(str(x) for x in row) for row in array), '\n')

sum = array_processor.process(array)

print("Sum of squares of positive even elements:", sum, '\n')
print("Processed array:")
print('\n'.join(' '.join(str(x) for x in row) for row in array))
