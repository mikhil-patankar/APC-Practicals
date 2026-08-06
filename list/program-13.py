# 13.	Accept 10 numbers and sort them in:
# •	Ascending order 
# •	Descending order

l = []

print("Enter 10 numbers.")
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    l.append(n)


print(f"Entered Numbers: {l}")
l.sort()
print(f"Ascending Order: {l}")
l.sort(reverse=True)
print(f"Descending Order: {l}")
