# Write a PYTHON program to sum the given sequence
#       1/ 0! + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

n = int(input("Enter a number: "))
sum = 0

def fact(num):
    f = 1
    for i in range(1, num+1):
        f = f * i
    return f

for i in range(n):
    sum += (1 / fact(i))

print(f"Sequence sum: {sum}")
