from utils import validate_string,handle_error
#main class for the author operations
class Author:
    def __init__(self, name=None, bio=None):
        self.name = name
        self.bio = bio
    @handle_error
    #function to add an author
    def add_author(self, authors):
        while True:
            name = input("Enter the author's name: ")
            if not validate_string(name):
                continue
            bio = input("Enter a short bio of the author: ")
            if not validate_string(bio):
                continue
            author = Author(name, bio)
            authors[name] = author
            print(f"Author '{name}' added successfully.")
            break
    @handle_error       
    #function to view an author if you input their name     
    def view_author(self, authors):
        name = input("Enter the author's name to view details: ")
        if name in authors:
            author = authors[name]
            print(f"Author Details: {author.name} - {author.bio}")
        else:
            print("Author not found.")
    @handle_error
    #function to display ALL authors
    def display_all_authors(self, authors):
        if authors:
            print("\nAll Authors:")
            for author in authors.values():
                print(f"{author.name}: {author.bio}")
        else:
            print("No authors available.")
