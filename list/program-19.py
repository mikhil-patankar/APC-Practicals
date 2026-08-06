# 19.	Store names of students present in class.
# Display:
# •	Total students 
# •	Search a students attendance 
# •	Add a new student 
# •	Remove an absent student 


students = []

def addStudents(name):
    students.append(name)
    return students

def delStudents(name):
    students.remove(name)

def searchStudents(name):
    if name in students:
        return "Present."
    else:
        return "Absent."

def displayStudents():
    print("Students Present List:")
    for student in students:
        print(f"{student}")

def totalStudents():
    return len(students)

option = 99

while(option != 0):
    print(
        """[1] Add a student 
[2] Remove an absent student 
[3] Search a student attendance
[4] Display Present students 
[5] Count total students
[0] Exit""")
    option = int(input("Enter your option: "))
    match option:
        case 1:
            name = input("Enter student name: ")
            addStudents(name)
        case 2:
            name = input("Enter student name: ")
            delStudents(name)
        case 3:
            name = input("Enter student name: ")
            print(searchStudents(name))
        case 4:
            displayStudents()
        case 5:
            print("Total Students:", totalStudents())
        case 0:
            print("Exiting...")
        case _:
            print("Unknown Option.")
    print()