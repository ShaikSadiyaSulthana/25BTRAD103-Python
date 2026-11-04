
# Library Management System Using OOP

class Book:

    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title, "issued successfully!")
        else:
            print(self.title, "is not available!")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title, "returned successfully!")
        else:
            print(self.title, "was not issued!")

    def display(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.title)
        print("Availability:", 
              "Available" if self.available else "Issued")


# Creating book objects
book1 = Book(101, "Python Programming")
book2 = Book(102, "Java Programming")

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book1.display()
        print()
        book2.display()

    elif choice == "2":
        book_id = int(input("Enter book ID: "))

        if book_id == 101:
            book1.issue_book()
        elif book_id == 102:
            book2.issue_book()
        else:
            print("Book not found!")

    elif choice == "3":
        book_id = int(input("Enter book ID: "))

        if book_id == 101:
            book1.return_book()
        elif book_id == 102:
            book2.return_book()
        else:
            print("Book not found!")

    elif choice == "4":
        print("Exiting Library System!")
        break

    else:
        print("Invalid choice!")
