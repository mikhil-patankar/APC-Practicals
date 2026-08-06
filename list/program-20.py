# 20.	Create a list of books.
# Implement:
# •	Add a new book 
# •	Search a book 
# •	Remove a book 
# •	Display all books 
# •	Count total books


books = []

def addBooks(name):
    books.append(name)
    return books

def delBooks(name):
    books.remove(name)

def searchBooks(name):
    if name in books:
        return "Exists."
    else:
        return "Does not Exists."

def displayBooks():
    print("Bookss List:")
    for book in books:
        print(f"{book}")

def totalBooks():
    return len(books)

option = 99

while(option != 0):
    print(
        """[1] Add a book 
[2] Delete a book 
[3] Search a book 
[4] Display all books 
[5] Count total books
[0] Exit""")
    option = int(input("Enter your option: "))
    match option:
        case 1:
            name = input("Enter book name: ")
            addBooks(name)
        case 2:
            name = input("Enter book name: ")
            delBooks(name)
        case 3:
            name = input("Enter book name: ")
            print(searchBooks(name))
        case 4:
            displayBooks()
        case 5:
            print("Total Books:", totalBooks())
        case 0:
            print("Exiting...")
        case _:
            print("Unknown Option.")
    print()