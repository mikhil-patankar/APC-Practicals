# Check whether one string is a rotation of another.
# Example: ABCD and CDAB -> Output: Yes

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and len(str1) > 0:
    temp = str1 + str1
    if str2 in temp:
        print("Output: Yes")
    else:
        print("Output: No")
else:
    print("Output: No")
