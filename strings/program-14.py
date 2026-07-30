# Convert the first letter of every word to uppercase.

sentence = input("Enter a sentence: ")
words = sentence.split()

title_cased = []
for word in words:
    if len(word) > 0:
        capitalized = word[0].upper() + word[1:].lower()
        title_cased.append(capitalized)

result = " ".join(title_cased)
print(f"Title case sentence: {result}")
