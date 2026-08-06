# 7.	Accept 10 numbers from the user and store them in a list. Calculate:
# •	Sum 
# •	Average 

l = []

print("Enter 10 numbers.")
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    l.append(n)


print(f"Entered Numbers: {l}")
print(f"Sum: {sum(l)}")
print(f"Average: {sum(l)/len(l)}")