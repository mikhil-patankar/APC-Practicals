
# Write a PYTHON program that prints  1 2 4 8 16 32 … n2

n = int(input("Enter a number: "))

x = 1
print(x, end=" ")

for i in range(n):
    if x*2 < n**2:
        x = x * 2
        print(x , end=" ")