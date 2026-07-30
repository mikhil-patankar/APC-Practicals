# Reverse the order of words in a sentence without changing the words themselves.
# Example:
# Input: Python is easy
# Output: easy is Python

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words[::-1]

result = " ".join(reversed_words)
print(f"Reversed sentence: {result}")
