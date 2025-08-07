class Library :
    book_list = []
    def __init__(self):
        pass
    
    def options(self):
        print("====Welcome to the Library===")
        print("\n")
        print("1. View All Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        print("\n")
        #print("Please enter your choice:")
        choice = int(input("Please enter your choice: "))
        return choice
    
    def enter_book(self, book):
        self.book_list.append(book)
        #print(f"Book '{book}' has been added to the library.")
    
class Book(Library):
    __book_id = 0
    __tittle = ""
    __author = ""
    __availability = True

    def __init__(self, book_id, tittle, author, availability) :
        super().__init__()
        self.__book_id = book_id
        self.__tittle = tittle
        self.__author = author
        self.__availability = availability
    
    def view_book_info(self):
        for book in self.book_list:
               print(f"Book ID: {book.__book_id}, Title: {book.__tittle}, Author: {book.__author}, Available: {'Yes' if book.__availability else 'No'}")
        print("\n")
    
    def borrow_book(self, id):
        for book in self.book_list:
            if book.__book_id == id and book.__availability:
                book.__availability = False
                return f"You have borrowed '{book.__tittle}'.\n"
        return "Book not available for borrowing.\n"
    
    def return_book(self, id):
        for book in self.book_list:
            if book.__book_id == id and not book.__availability:
                book.__availability = True
                return f"You have returned '{book.__tittle}'.\n"
        return "Book not found or already available.\n"

    
book1 = Book(1, "1984", "George Orwell", True)
book1.enter_book(book1)
book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", True)
book2.enter_book(book2)
book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald", True)
book3.enter_book(book3)
book4 = Book(4, "Marhaba, Javascript", "Jonker Mahbub", True)
book4.enter_book(book4)
book5 = Book(5, "The Catcher in the Rye", "J.D. Salinger", True)
book5.enter_book(book5)
book6 = Book(6, "Pride and Prejudice", "Jane Austen", True)
book6.enter_book(book6)
book7 = Book(7, "The Hobbit", "J.R.R. Tolkien", True)
book7.enter_book(book7)
book8 = Book(8, "Fahrenheit 451", "Ray Bradbury", True)
book8.enter_book(book8)
book9 = Book(9, "Brave New World", "Aldous Huxley", True)
book9.enter_book(book9)
book10 = Book(10, "The Alchemist", "Paulo Coelho", True)
book10.enter_book(book10)

#print(book1.book_id)

while True:
    My_Library = Library()
    choice = My_Library.options()
    #print("You selected option:", choice)
    if choice == 1:
        print(book1.view_book_info())
    elif choice == 2:
        book_id = int(input("Enter Book ID to borrow: "))
        print(book1.borrow_book(book_id))
    elif choice == 3:
        book_id = int(input("Enter Book ID to return: "))
        print(book1.return_book(book_id))
    elif choice == 4:
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")





