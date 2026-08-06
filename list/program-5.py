# 5.	Create a list of student names. Remove:
# •	First student 
# •	Last student 
# •	A specific student by name 

students = ["raju", "ramesh", "yogi", "ramu"]
print(f"Students List: {students}")

students = students[1:]
print("Removed: First element")
print(f"Students List: {students}")

students.pop()
print("Removed: Last element")
print(f"Students List: {students}")

name = "yogi"
students.remove(name)
print("Removed:", name)
print(f"Students List: {students}")