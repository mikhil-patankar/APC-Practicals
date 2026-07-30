# Validate a password based on these conditions:
# - Minimum 8 characters
# - At least one uppercase letter
# - One lowercase letter
# - One digit
# - One special character

password = input("Enter a password: ")

has_min_len = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if has_min_len and has_upper and has_lower and has_digit and has_special:
    print("Password is Valid.")
else:
    print("Password is Invalid. Requirements:")
    if not has_min_len:
        print("- Minimum 8 characters")
    if not has_upper:
        print("- At least one uppercase letter")
    if not has_lower:
        print("- At least one lowercase letter")
    if not has_digit:
        print("- At least one digit")
    if not has_special:
        print("- At least one special character")
