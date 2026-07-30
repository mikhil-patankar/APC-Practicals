# Write a PYTHON program to check the entered  number is palindrome or not

n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")
