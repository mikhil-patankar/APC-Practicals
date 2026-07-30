# Write a PYTHON program to print smallest of n numbers

n = int(input("How many numbers do you want to enter? "))

if n > 0:
    i = 1
    num = float(input(f"Enter number {i}: "))
    smallest = num
    i += 1
    while i <= n:
        num = float(input(f"Enter number {i}: "))
        if num < smallest:
            smallest = num
        i += 1

    print(f"The smallest number is: {smallest}")
else:
    print("Invalid count of numbers.")
