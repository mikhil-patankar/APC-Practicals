print("Progarm to check if a character is a vowel")

vowels = ["a", "e", "i", "o", "u"]

c = input("Enter a character: ")

if c.lower() in vowels:
    print(f"{c} is a vowel.")
else:
    print(f"{c} is not a vowel.")