# Reverse the given string without using built-in reverse functions.

s = input("Enter a string: ")
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s

print(f"Reversed string: {reversed_s}")
