from auth.login import register_user, login_user
from systems.hospital import hospital_menu
from systems.store import store_menu


def main_menu():
    while True:
        print("\n==============================")
        print("Welcome to WhiteHub CLI")
        print("==============================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            username = login_user()

            if username is not None:
                dashboard(username)

        elif choice == "2":
            register_user()

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


def dashboard(username):
    while True:
        print("\n==============================")
        print(f"Dashboard - Hello {username}")
        print("==============================")
        print("1. Hospital System")
        print("2. Store System")
        print("3. Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            hospital_menu(username)

        elif choice == "2":
            store_menu(username)

        elif choice == "3":
            print("Logged out.")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()