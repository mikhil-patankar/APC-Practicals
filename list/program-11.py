# 11.	Create a list of 10 numbers and display:
# •	First 5 elements 
# •	Last 5 elements 
# •	Middle 4 elements 
# •	Alternate elements 

numbers = [465,84,8,55,41,51,18,1,84,84]

print(f"First 5 Elements: {numbers[:5]}")
print(f"Last 5 Elements: {numbers[-5:]}")
print(f"Mid 4 Elements: {numbers[3:-3]}")
print(f"Alternate Elements: {numbers[::2]}")
print(f"Reversed List: {numbers[::-1]}")