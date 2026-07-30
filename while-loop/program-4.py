# Write a PYTHON program to print sum of natural numbers up to n

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f"Sum: {sum}")
