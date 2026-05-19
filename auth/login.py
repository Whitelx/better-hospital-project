from utils.json_utils import load_json, save_json
from auth.security import hash_password, check_password

USER_FILE = "data/users.json"


def register_user():
    print("\n=== Register ===")

    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return

    users = load_json(USER_FILE)

    for user in users:
        if user["username"] == username:
            print("Username already exists.")
            return

    hashed = hash_password(password)

    new_user = {
        "username": username,
        "password": hashed,
        "role": "user"
    }

    users.append(new_user)
    save_json(USER_FILE, users)

    print("Account created successfully.")


def login_user():
    print("\n=== Login ===")

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    users = load_json(USER_FILE)

    for user in users:
        if user["username"] == username:
            saved_password = user["password"]

            if check_password(password, saved_password):
                print("Login successful.")
                return username
            else:
                print("Wrong password.")
                return None

    print("User not found.")
    return None