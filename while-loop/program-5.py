# Write a PYTHON program to print sum of odd numbers up to n

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    if i % 2 != 0:
        sum += i
    i += 1

print(f"Sum of odd numbers: {sum}")
