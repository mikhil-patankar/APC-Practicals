# Check whether the entered string is a palindrome.

s = input("Enter a string: ")
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

if s == reversed_s:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")
