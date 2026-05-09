expenses = []

while True:
    print("\n1. Add expense")
    print("2. View summary")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))

        expenses.append({
            "category": category,
            "amount": amount
        })

    elif choice == "2":
        total = 0

        print("\nExpenses:")

        for expense in expenses:
            print(f"{expense['category']}: ${expense['amount']:.2f}")
            total += expense["amount"]

        print(f"\nTotal: ${total:.2f}")

    elif choice == "3":
        break

    else:
        print("Invalid choice")
