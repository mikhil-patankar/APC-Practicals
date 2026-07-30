# Print the first and last character of a string.

s = input("Enter a string: ")

if len(s) > 0:
    print(f"First character: {s[0]}")
    print(f"Last character: {s[-1]}")
else:
    print("String is empty.")
