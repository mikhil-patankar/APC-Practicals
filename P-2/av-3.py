print("Program to find smallest of three numbers.")

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))


if n1 <= n2 and n1 <= n3:
    print(f"{n1} is smallest.")
elif n2 <= n1 and n2 <= n3:
    print(f"{n2} is smallest.")
else:
    print(f"{n3} is smallest.")