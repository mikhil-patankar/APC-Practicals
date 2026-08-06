# 6.	Write a program to find the largest and smallest number in a list without using max() or min().


l = [54, 655, 83, 5, 23, 7, 84, 3, 487]

def largest(l):
    if len(l) > 0:
        max = l[0]
        for i in l:
            if i > max:
                max = i
        return max
    return None


def smallest(l):
    if len(l) > 0:
        min = l[0]
        for i in l:
            if i < min:
                min = i
        return min
    return None

print("List: ", l)

print(f"Largest: {largest(l)}")
print(f"Smallest: {smallest(l)}")