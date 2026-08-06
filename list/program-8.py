# 8.	Store 15 integers in a list. Count how many numbers are:
# •	Even 
# •	Odd


numbers = [465,84,8,55,41,51,18,1,84,84,8,1,5,8,48]

print(f"Numbers: {numbers}")

odd = 0
even = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Odd Numbers: {odd}\nEven Numbers: {even}")