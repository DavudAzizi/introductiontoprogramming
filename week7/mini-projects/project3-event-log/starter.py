contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")

        contacts[name] = phone

    elif choice == "2":
        name = input("Search name: ")

        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
