# 30.	Store patient names and ages using lists.
# Perform:
# [] Add a patient 
# [] Delete a patient 
# [] Search a patient 
# [] Display all patients 
# [] Count total patients

patients = []

def addPatient(name):
    patients.append(name)
    return patients

def delPatient(name):
    patients.remove(name)

def searchPatient(name):
    if name in patients:
        return "Exists."
    else:
        return "Does not Exists."

def displayPatients():
    print("Patients List:")
    for patient in patients:
        print(f"{patient}")

def totalPatients():
    return len(patients)

option = 99

while(option != 0):
    print(
        """[1] Add a patient 
[2] Delete a patient 
[3] Search a patient 
[4] Display all patients 
[5] Count total patients
[0] Exit""")
    option = int(input("Enter your option: "))
    match option:
        case 1:
            name = input("Enter patient name: ")
            addPatient(name)
        case 2:
            name = input("Enter patient name: ")
            delPatient(name)
        case 3:
            name = input("Enter patient name: ")
            searchPatient(name)
        case 4:
            displayPatients()
        case 5:
            print("Total Patients:", totalPatients())
        case 0:
            print("Exiting...")
        case _:
            print("Unknown Option.")
    print()