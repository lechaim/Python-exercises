# 1. Library Management System (Recommended)

# Build a console application where users can:

# Add books 
# Borrow books
# Return books
# Search by title or author
# Display all available books
# Save and load the library from a file

# Programming fundamentals you'll use:

# Variables
# Functions
# Lists and dictionaries
# Loops
# if statements
# File I/O
# Exception handling


# A dictionary containing worker profiles
Books = {
    0: {"name": "1984","author": "George Orwell", "availability": 0},
    1: {"name": "Pride and Prejudice", "author": "Jane Austen", "availability": 1},
    2: {"name": "To Kill a Mockingbird","author": "Harper Lee", "availability": 1}
}

#functions

def add_book():

    in_book_name = input("Please add the book's name ")
    in_author = input("Please add the author's name ")
    in_availability = input("Please add the number of books ")

    Books [len(Books)] = {"name": in_book_name,"author": in_author, "availability": in_availability}
    print(Books)

def borrow_book():

    in_book_name = input("Please add the book's name ")
    in_author = input("Please add the author's name ")

    for id in range(len(Books)): # id is an unique code, this part will see if the book is available
        if (Books[id]["name"] == in_book_name or Books[id]["author"] == in_author) and Books[id]["availability"] >= 1:
            print("The book is available")
            break
        else:
            print("The book is not available")
            break

def return_book():
        
        in_book_name = input("Please add the book's name ")
        in_author = input("Please add the author's name ")

        for id in range(len(Books)):
            if (Books[id]["name"] == in_book_name or Books[id]["author"] == in_author):
                    Books[id]["availability"] += 1
                
def available_books():
     
    for id in range(len(Books)):
        if  Books[id]["availability"] == 0:
                pass
        else:
                print(f"{Books[id]["name"]} - {Books[id]["author"]}; available copies: {Books[id]["availability"]} \n")

def file():
     with open("Available Books.txt", "w") as file:
          for id in range(len(Books)):
                  if  Books[id]["availability"] == 0:
                          pass
                  else:
                        file.write(f"{Books[id]["name"]} - {Books[id]["author"]}; available copies: {Books[id]["availability"]} \n")
          
          
     

while True:

    numbers_for_options = [1,2,3,4,5]
    
    options = input("Select an option: ")
    if int(options) not in numbers_for_options:
        print("Please select an option using numbers 1 to 5: ")

    else:
         match options:
            case '1':
                add_book()
            case '2':
                borrow_book()
            case '3':
                return_book()
            case '4':
                available_books()
            case '5':
                file()
                   
                   
    
        