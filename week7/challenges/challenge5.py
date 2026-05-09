accounts = {}

while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View accounts")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Account holder: ")

        if name not in accounts:
            accounts[name] = 0
            print("Account created")
        else:
            print("Account already exists")

    elif choice == "2":
        name = input("Account holder: ")

        if name in accounts:
            amount = float(input("Deposit amount: "))
            accounts[name] += amount
            print("Deposit successful")
        else:
            print("Account not found")

    elif choice == "3":
        name = input("Account holder: ")

        if name in accounts:
            amount = float(input("Withdraw amount: "))

            if amount <= accounts[name]:
                accounts[name] -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        else:
            print("Account not found")

    elif choice == "4":
        print("\nAccounts:")

        for name, balance in accounts.items():
            print(f"{name}: ${balance:.2f}")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
