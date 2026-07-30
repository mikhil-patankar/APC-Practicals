# Count how many times a specific word appears in a sentence.

sentence = input("Enter a sentence: ")
target_word = input("Enter word to count: ")

words = sentence.split()
count = 0

for word in words:
    if word.strip(".,!?\"'()[]{}") == target_word:
        count += 1

print(f"The word '{target_word}' appears {count} times.")
