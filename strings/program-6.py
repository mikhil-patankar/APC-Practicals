# Replace all occurrences of a given character with another character.

s = input("Enter a string: ")
old_char = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = ""
for char in s:
    if char == old_char:
        result += new_char
    else:
        result += char

print(f"Modified string: {result}")
