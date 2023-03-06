# Welcome to the password manager.
# This program is designed to help you keep your passwords safe.
# It will help you store your passwords in a file and then be able to access them.
# ALL PASSWORDS ARE ENCRYPTED.
# It will also help you add new passwords to the file.
# It will also help you delete passwords from the file.
# It will also help you update passwords in the file.
# It will also help you search for passwords in the file.
# It will also help you see all the passwords in the file.
# It will also help you view all decrypted passwords in the file.

# Import the encryption machine.
import pyEncryptorMachine as enc


def add():
    print("You have chosen to add a new password.")
    print("Please enter the following details:")

    site_name = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # enc.encode_password(password)

    # Write the data to the file.
    with open("passwords.txt", "a") as file:
        file.write(
            site_name + "|" + username + "|" + enc.encode_password(password) + "\n"
        )


# This function will be used to view all decrypted passwords.
def view():
    # View all the original passwords in the file.
    print(" You have chosen to reveal all encrypted passwords in the file.")
    with open("passwords.txt", "r") as file:
        for line in file:
            site, user, pwd = line.rstrip().split("|")
            print(
                "\nSite Name:" + site,
                "\nUsername: " + user,
                "\nPassword: " + enc.decode_password(pwd),
            )
            print("==================================================")


# This function will be used to update a password.
def update():
    pass
    print("You have chosen to update a password.")
    update_record = input("Which site's password do you want to update?").lower()
    new_pass = input("Enter the new password: ")
    with open("passwords.txt", "r") as file:
        list_of_lines = file.readlines()
        for line in list_of_lines:
            if update_record in line:
                site, user, pwd = line.rstrip().split("|")
                ind = list_of_lines.index(line)
                list_of_lines[ind] = (
                    site + "|" + user + "|" + enc.encode_password(new_pass) + "\n"
                )
                with open("passwords.txt", "w") as file:
                    file.writelines(list_of_lines)
                    print("Password updated successfully.")


# This function will be used to delete a record.
def delete():
    print("You have chosen to delete a record.")
    delte_record = input("Which site's password do you want to delete?").lower()
    with open("passwords.txt", "r") as file:
        list_of_lines = file.readlines()
        for line in list_of_lines:
            if delte_record in line:
                ind = list_of_lines.index(line)
                del list_of_lines[ind]
                with open("passwords.txt", "w") as file:
                    file.writelines(list_of_lines)
                    print("Password deleted successfully.")


# This function will be used to search a password.
def search():
    print("You have chosen to search for a password.")
    search_mode = input("How do you want to search?(Site, Username)").lower()
    if search_mode == "site":
        site_name = input("Enter the site name: ")
        with open("passwords.txt", "r") as file:
            list_of_lines = file.readlines()
            for line in list_of_lines:
                if site_name in line:
                    site, user, pwd = line.rstrip().split("|")
                    print(
                        "\nSite Name:" + site,
                        "\nUsername: " + user,
                        "\nPassword: " + pwd + "\n",
                    )
    elif search_mode == "username":
        username = input("Enter the username: ")
        with open("passwords.txt", "r") as file:
            list_of_lines = file.readlines()
            for line in list_of_lines:
                if username in line:
                    site, user, pwd = line.rstrip().split("|")
                    print(
                        "\nSite Name:" + site,
                        "\nUsername: " + user,
                        "\nPassword: " + pwd + "\n",
                    )
    else:
        print("Invalid input.")


# This function will be used to see all the passwords in the file.
def view_all():
    # View all the passwords in the file.
    print("You have chosen to view all the passwords.")
    with open("passwords.txt", "r") as file:
        for line in file:
            site, user, pwd = line.rstrip().split("|")
            print(
                "\nSite Name:" + site,
                "\nUsername: " + user,
                "\nPassword: " + pwd,
            )

            print("==================================================")


# vairable for a first time user.
is_first_time = True

# Print the menu for first time user.
if is_first_time:
    print("Welcome to the password manager.")
    print("Please choose from the following options:")
    print("Add: Add a new password.")
    print("View: View the last password added.")
    print("Update: Update a password.")
    print("Delete: Delete a password.")
    print("Search: Search for a password.")
    print("All: View all the passwords.")
    print("Quit: Quit the program.")

# Ask the user to choose an option.
# Use loop to iterate the menu.
while True:
    # Display the menu.
    print(
        "Would you like to create a new password or view an existing password ? (Add, View, Update, Delete, Search, All, Quit)"
    )
    mode = input("Enter the mode: ").lower()

    # Quit the program.
    if mode == "quit":
        if is_first_time:
            print("So soon? I can save your passwords safely for you.")
            is_first_time = False
            break
        else:
            print("Your passwords safe with me.")
            break

    # Add a new password.
    elif mode == "add":
        is_first_time = False
        add()

    # View a password.
    elif mode == "view":
        is_first_time = False
        view()

    # Update a password.
    elif mode == "update":
        is_first_time = False
        update()

    # Delete a password.
    elif mode == "delete":
        is_first_time = False
        delete()

    # Search for a password.
    elif mode == "search":
        is_first_time = False
        search()

    # View all the passwords in the file.
    elif mode == "all":
        is_first_time = False
        view_all()

    # If the user enters an invalid mode.
    else:
        print("Please enter a valid mode.")
        continue

# End of the program.