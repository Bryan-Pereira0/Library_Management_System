import re

#used to validate all input strings
def validate_string(input_str):
    if re.match("^[a-zA-Z0-9 ]+$", input_str):
        return input_str
    else:
        raise ValueError("Invalid input format.")

#used to handle all errors
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
    return wrapper
