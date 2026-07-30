# Write a PYTHON program to print the largest of n numbers

n = int(input("How many numbers do you want to enter? "))

if n > 0:
    i = 1
    num = float(input(f"Enter number {i}: "))
    largest = num
    i += 1
    while i <= n:
        num = float(input(f"Enter number {i}: "))
        if num > largest:
            largest = num
        i += 1

    print(f"The largest number is: {largest}")
else:
    print("Invalid count of numbers.")
