# Count the frequency of every word in a paragraph.

import string

paragraph = input("Enter a paragraph: ")

cleaned = paragraph.translate(str.maketrans("", "", string.punctuation)).lower()
words = cleaned.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequency Dictionary:")
for word, count in word_freq.items():
    print(f"'{word}': {count}")
