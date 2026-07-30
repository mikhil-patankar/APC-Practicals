# Check whether a given substring exists in the main string.

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring to search: ")

if sub_str in main_str:
    print(f"Substring '{sub_str}' exists in the main string.")
else:
    print(f"Substring '{sub_str}' does not exist in the main string.")
