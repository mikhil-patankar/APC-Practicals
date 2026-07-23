print("Program to check if a given year is a leap year")

n = int(input("Enter year: "))

if (n % 4 == 0):
    print(f"Year {n} is a leap year.")
else:
    print(f"Year {n} is not a leap year.")