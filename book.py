from utils import validate_string, handle_error
#main class for the book operations
class Book:
    def __init__(self, title=None, author=None, genre=None, publication_date=None, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.available = available
    #function to add books
    @handle_error
    def add_book(self, books):
        while True:
            title = input("Enter the book title: ")
            if not validate_string(title):
                continue
            genre = input("Enter the genre of the book: ")
            if not validate_string(genre):
                continue
            author = input("Enter the author's name: ")
            publication_date = input("Enter the publication date (DD-MM-YYYY): ")
            if not publication_date:
                print("Publication date cannot be empty.")
                continue
            books[title] = Book(title, author, genre, publication_date)
            print(f"Book '{title}' added successfully.")
            break
    #function to borrow books
    @handle_error
    def borrow_book(self, books):
        title = input("Enter the title of the book to borrow: ")
        if title in books and books[title].available:
            books[title].available = False
            print(f"You have borrowed '{title}'.")
        else:
            print("Book not available or doesn't exist.")
    #function to return a borrowed book
    @handle_error
    def return_book(self, books):
        title = input("Enter the title of the book to return: ")
        if title in books and not books[title].available:
            books[title].available = True
            print(f"Book '{title}' returned successfully.")
        else:
            print("This book was not borrowed or doesn't exist.")
    #function to search through all books
    @handle_error
    def search_book(self, books):
        title = input("Enter the title of the book to search: ")
        if title in books:
            book = books[title]
            print(f"Book found: {book.title} by {book.author} (Genre: {book.genre}, Published on: {book.publication_date})")
        else:
            print("Book not found.")
    #function to display all books
    @handle_error
    def display_all_books(self, books):
        if books:
            print("\nAll Books:")
            for book in books.values():
                status = "Available" if book.available else "Not Available"
                print(f"{book.title} by {book.author} ({book.genre}) - Published on: {book.publication_date} - {status}")
        else:
            print("No books available.")
