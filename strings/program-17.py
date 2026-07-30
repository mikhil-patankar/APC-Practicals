# Check whether two strings are anagrams.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

clean1 = sorted(str1.replace(" ", "").lower())
clean2 = sorted(str2.replace(" ", "").lower())

if clean1 == clean2:
    print(f"'{str1}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams.")
