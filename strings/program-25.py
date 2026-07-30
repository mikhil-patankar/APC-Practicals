# Find the second most frequently occurring character.

s = input("Enter a string: ")

if not s:
    print("Empty string.")
else:
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_freq) < 2:
        print("Not enough unique characters to find second most frequent.")
    else:
        second_char, count = sorted_freq[1]
        print(f"Second most frequent character: '{second_char}' (Appears {count} times)")
