# Write a program to input a string and display its length without using the len() function.

s = input("Enter a string: ")
length = 0
for char in s:
    length += 1

print(f"Length of the string: {length}")
