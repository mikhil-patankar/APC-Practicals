# 18.	Create a shopping cart using a list.
# Perform:
# •	Add item 
# •	Remove item 
# •	Search item 
# •	Display cart 
# •	Count total items


carts = []

def addCart(name):
    carts.append(name)
    return carts

def delCart(name):
    carts.remove(name)

def searchCart(name):
    if name in carts:
        return "Exists."
    else:
        return "Does not Exists."

def displayCarts():
    print("Carts List:")
    for cart in carts:
        print(f"{cart}")

def totalCarts():
    return len(carts)

option = 99

while(option != 0):
    print(
        """[1] Add a cart 
[2] Delete a cart 
[3] Search a cart 
[4] Display all carts 
[5] Count total carts
[0] Exit""")
    option = int(input("Enter your option: "))
    match option:
        case 1:
            name = input("Enter cart name: ")
            addCart(name)
        case 2:
            name = input("Enter cart name: ")
            delCart(name)
        case 3:
            name = input("Enter cart name: ")
            print(searchCart(name))
        case 4:
            displayCarts()
        case 5:
            print("Total Carts:", totalCarts())
        case 0:
            print("Exiting...")
        case _:
            print("Unknown Option.")
    print()