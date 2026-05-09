expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Total")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Expense amount: "))
        expenses.append(amount)

    elif choice == "2":
        total = sum(expenses)
        print(f"Total expenses: ${total:.2f}")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
