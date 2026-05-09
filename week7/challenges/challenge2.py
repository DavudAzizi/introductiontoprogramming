inventory = {}

while True:
    print("\n1. Add item")
    print("2. View inventory")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        item = input("Item name: ")
        quantity = int(input("Quantity: "))

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

    elif choice == "2":
        print("\nInventory:")

        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
