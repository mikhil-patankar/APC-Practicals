
print("Program to insure a driver.")

married = input("Are you married: ")

if married not in ["yes", "y", "no", "n"]:
    print("Invalid married status.")
    exit()

gender = input("Enter your Gender: ")

if gender not in ["m", "male", "f", "female"]:
    print("Invalid gender status.")
    exit()

age = int(input("Enter your age: "))
eligible = True

if (married in ["no", "n"]):
    if gender == "m" or gender == "male":
        if age <=30:
            eligible = False

    elif gender == "f" or gender == "female":
        if age <=25:
            eligible = False

if eligible:
    print("Driver is Eligible to be insured.")
else:
    print("Driver could not be insured.")