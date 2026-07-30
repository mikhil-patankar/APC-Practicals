# Remove all spaces from the input string.

s = input("Enter a string: ")
result = ""

for char in s:
    if char != " ":
        result += char

print(f"String without spaces: {result}")
