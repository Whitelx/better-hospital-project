from utils.json_utils import load_json, save_json
from auth.security import hash_password, check_password

USER_FILE = "data/users.json"

def register_user():

    print("\n=== Register ===")
    
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return
    
    users = load_json(USER_FILE)

    for user in users:
        if user["username"] == username:
            print("Username already exists")
            return
        
    hashed = hash_password(password)

    new_user = {
        "username": username,
        "password": password,
        "role": "user"
    }

    user.append(new_user)
    save_json(USER_FILE, users)

    print("Account created successfully.")


def login_user():

    print("\n=== Login ===")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    users = load_json(USER_FILE)

    for user in users:
        if user["username"] == username:
            print("Login successful.")
            return username
        else:
            print("Wrong username.")
            return None
        
    print("User not found.")
    return None