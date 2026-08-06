# 22. Find common elements between two lists.


l1 = [54, 655, 83, 5, 23, 7, 84, 3, 487]

l2 = [489, 198, 54, 158, 34, 48, 84, 3, 487]

print(f"List 1: {l1}")
print(f"List 2: {l2}")


print(f"Common Elements: {list(set(l1) & set(l2))}")