# Remove duplicate characters while maintaining the original order.

s = input("Enter a string: ")
result = ""
seen = set()

for char in s:
    if char not in seen:
        seen.add(char)
        result += char

print(f"String after removing duplicates: {result}")
