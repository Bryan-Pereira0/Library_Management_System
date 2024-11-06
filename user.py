from utils import validate_string,handle_error
#main class for the user operations
class User:
    def __init__(self, name=None, user_id=None):
        self.name = name
        self.user_id = user_id
    @handle_error
    #function to add users 
    def add_user(self, users):
        while True:
            name = input("Enter the user's name: ")
            if not validate_string(name):
                continue
            user_id = input("Enter the user ID: ")
            if not validate_string(user_id):
                continue
            user = User(name, user_id)
            users[user_id] = user
            print(f"User '{name}' added successfully.")
            break
    @handle_error
    #function to view user if you input a matching ID
    def view_user(self, users):
        user_id = input("Enter the user ID to view details: ")
        if user_id in users:
            user = users[user_id]
            print(f"User Details: {user.name} (User ID: {user.user_id})")
        else:
            print("User not found.")
    @handle_error
    #function to display ALL users
    def display_all_users(self, users):
        if users:
            print("\nAll Users:")
            for user in users.values():
                print(f"{user.name} (User ID: {user.user_id})")
        else:
            print("No users available.")
