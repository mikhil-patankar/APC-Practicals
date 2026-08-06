# 9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Amravati", "Akola", "Pune", "Kolhapur", "Mumbai"]

print(f"Cities: {cities}")

c = input("Enter a city to check if it exists in list: ")

if c in cities:
    print("City is in list.")
else:
    print("City is not in list.")
    