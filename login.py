def register():
    username = input("Create a username: ")
    password = input("Create a password: ")
    
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    
    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    with open("users.txt", "r") as file:
        for line in file:
            saved_user, saved_pass = line.strip().split(",")
            if username == saved_user and password == saved_pass:
                print("Login successful!")
                return
    print("Login failed. Check your credentials.")


def main():
    print("1. Register")
    print("2. Login")
    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
