from book import Book
from user import User
from author import Author
from utils import handle_error

class MainUI:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.authors = {}
    #function that displays the main UI and connects to all operations
    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Select an option: ")

            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    #book operation UI
    @handle_error
    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                Book().add_book(self.books)
            elif choice == '2':
                Book().borrow_book(self.books)
            elif choice == '3':
                Book().return_book(self.books)
            elif choice == '4':
                Book().search_book(self.books)
            elif choice == '5':
                Book().display_all_books(self.books)
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")
    #user operation UI
    @handle_error
    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                User().add_user(self.users)
            elif choice == '2':
                User().view_user(self.users)
            elif choice == '3':
                User().display_all_users(self.users)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    #author operation UI
    @handle_error
    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                Author().add_author(self.authors)
            elif choice == '2':
                Author().view_author(self.authors)
            elif choice == '3':
                Author().display_all_authors(self.authors)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please try again.")