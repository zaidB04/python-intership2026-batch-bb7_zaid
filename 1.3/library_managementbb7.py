# ==========================================================
# DigolTech - Python Internship Assessment 2026
# Section C: Coding Assessment - OOP & Functions
# Q1: Library Management System
# Total Marks: 25
# ==========================================================


# ----------------------------------------------------------
# 1. CREATE BOOK CLASS
# ----------------------------------------------------------

class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True


# ----------------------------------------------------------
# 2. CREATE LIBRARY CLASS
# ----------------------------------------------------------

class Library:

    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):

        if self.search_book(book.book_id):
            print("Error: Book ID already exists!")
        else:
            self.books.append(book)
            print("Book added successfully!")

    # View all books
    def view_books(self):

        print("\n========== BOOK LIST ==========")

        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:

            print("\nBook ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)

            if book.is_available:
                print("Status: Available")
            else:
                print("Status: Issued")

            print("-------------------------------")

    # Search book using ID
    def search_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                return book

        return None

    # Issue a book
    def issue_book(self, book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Error: Book not found!")

        elif not book.is_available:
            print("Sorry! This book is already issued.")

        else:
            book.is_available = False
            print("Book issued successfully!")

    # Return a book
    def return_book(self, book_id):

        book = self.search_book(book_id)

        if book is None:
            print("Error: Book not found!")

        elif book.is_available:
            print("Sorry! This book has not been issued.")

        else:
            book.is_available = True
            print("Book returned successfully!")


# ----------------------------------------------------------
# 3. CREATE MAIN FUNCTION
# ----------------------------------------------------------

def main():

    library = Library()

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")

        print("\n1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        # Option 1: Add Book
        if choice == "1":

            try:
                book_id = int(input("Enter Book ID: "))

                title = input("Enter Book Title: ").strip()
                author = input("Enter Author Name: ").strip()

                if not title or not author:
                    print("Error: Title and author cannot be empty!")
                else:
                    book = Book(book_id, title, author)
                    library.add_book(book)

            except ValueError:
                print("Error: Book ID must be a valid number!")

        # Option 2: View All Books
        elif choice == "2":

            library.view_books()

        # Option 3: Search Book
        elif choice == "3":

            try:
                book_id = int(input("Enter Book ID: "))

                book = library.search_book(book_id)

                if book is None:
                    print("Error: Book not found!")

                else:
                    print("\nBook Found!")
                    print("Book ID:", book.book_id)
                    print("Title:", book.title)
                    print("Author:", book.author)

                    if book.is_available:
                        print("Status: Available")
                    else:
                        print("Status: Issued")

            except ValueError:
                print("Error: Book ID must be a valid number!")

        # Option 4: Issue Book
        elif choice == "4":

            try:
                book_id = int(input("Enter Book ID: "))
                library.issue_book(book_id)

            except ValueError:
                print("Error: Book ID must be a valid number!")

        # Option 5: Return Book
        elif choice == "5":

            try:
                book_id = int(input("Enter Book ID: "))
                library.return_book(book_id)

            except ValueError:
                print("Error: Book ID must be a valid number!")

        # Option 6: Exit
        elif choice == "6":

            print("Thank you for using Library Management System!")
            break

        # Invalid Menu Choice
        else:

            print("Invalid choice! Please select between 1 and 6.")


# ----------------------------------------------------------
# 4. PROGRAM EXECUTION
# ----------------------------------------------------------

if __name__ == "__main__":
    main()


# ==========================================================
# END OF LIBRARY MANAGEMENT SYSTEM
# ==========================================================