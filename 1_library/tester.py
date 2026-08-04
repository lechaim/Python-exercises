

Books = {
    0: {"name": "1984","author": "George Orwell", "availability": 1},
    1: {"name": "Pride and Prejudice", "author": "Jane Austen", "availability": 1},
    2: {"name": "To Kill a Mockingbird","author": "Harper Lee", "availability": 1}
}




def borrow_book():

    in_book_name = input("Please add the book's name ")

    found = False

    for id in range(len(Books)): # id is an unique code, this part will see if the book is available
        if Books[id]["name"] == in_book_name and Books[id]["availability"] >= 1:
            found = True



    if found:
        Books[id]["availability"] -= 1
        print("Book borrowed succesfully")

    else:
        print("The book is not available")

borrow_book()