import hashlib
import os
import getpass

USER_DATA_FILE = 'users.txt'


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Choose a username: ")
    if user_exists(username):
        print("Username already exists.")
        return
    password = getpass.getpass("Choose a password: ")
    hashed = hash_password(password)
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f"{username},{hashed}\n")
    print("Registration successful!")


def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    hashed = hash_password(password)

    if not os.path.exists(USER_DATA_FILE):
        print("No users registered yet.")
        return False

    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(',')
            if stored_user == username and stored_hash == hashed:
                print("Login successful!")
                return True

    print("Invalid username or password.")
    return False


def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            stored_user, _ = line.strip().split(',')
            if stored_user == username:
                return True
    return False


def main():
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
