# Write a PYTHON program to find the sum of digits of given number

n = int(input("Enter a number: "))
temp = abs(n)
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print(f"Sum of digits of {n} is: {sum_digits}")
