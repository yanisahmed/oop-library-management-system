from abc import ABC, abstractmethod

class Library(ABC):
    book_list = []

    def __init__(self):
        pass

    def options(self):
        print("==== Welcome to the Library ====")
        print("\n1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit\n")
        choice = int(input("Please enter your choice: "))
        return choice

    def enter_book(self, book):
        self.book_list.append(book)

    @abstractmethod
    def view_book(self):
        pass

    @abstractmethod
    def borrow_book(self, id):
        pass

    @abstractmethod
    def return_book(self, id):
        pass

class Book(Library):
    def __init__(self, book_id, title, author, availability=True):
        super().__init__()
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def view_book(self):
        print("\n=== Book List ===")
        for book in self.book_list:
            status = 'Yes' if book.availability else 'No'
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Available: {status}")
        print()

    def borrow_book(self, id):
        for book in self.book_list:
            if book.book_id == id:
                if book.availability:
                    book.availability = False
                    return f"You have borrowed '{book.title}'.\n"
                else:
                    return "Book is already borrowed.\n"
        return "Book not found.\n"

    def return_book(self, id):
        for book in self.book_list:
            if book.book_id == id:
                if not book.availability:
                    book.availability = True
                    return f"You have returned '{book.title}'.\n"
                else:
                    return "Book was not borrowed.\n"
        return "Book not found.\n"

# Instantiate a single Book manager
library_manager = Book(0, "", "")

# Add books to the shared book list
books_data = [
    (1, "1984", "George Orwell"),
    (2, "To Kill a Mockingbird", "Harper Lee"),
    (3, "The Great Gatsby", "F. Scott Fitzgerald"),
    (4, "Marhaba, Javascript", "Jonker Mahbub"),
    (5, "The Catcher in the Rye", "J.D. Salinger"),
    (6, "Pride and Prejudice", "Jane Austen"),
    (7, "The Hobbit", "J.R.R. Tolkien"),
    (8, "Fahrenheit 451", "Ray Bradbury"),
    (9, "Brave New World", "Aldous Huxley"),
    (10, "The Alchemist", "Paulo Coelho"),
]

for data in books_data:
    book = Book(*data)
    library_manager.enter_book(book)

# Main loop
while True:
    choice = library_manager.options()
    
    if choice == 1:
        library_manager.view_book()
    elif choice == 2:
        book_id = int(input("Enter Book ID to borrow: "))
        print(library_manager.borrow_book(book_id))
    elif choice == 3:
        book_id = int(input("Enter Book ID to return: "))
        print(library_manager.return_book(book_id))
    elif choice == 4:
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
