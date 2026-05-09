# Project 5 — Mini Shopping Cart
# Author: Davud Azizi

menu = {
    1: ("Apple", 0.50),
    2: ("Banana", 0.30),
    3: ("Milk", 1.20),
    4: ("Bread", 2.00),
}

cart = {}
total = 0.0

print("--- Shop Menu ---")
for number, item in menu.items():
    name, price = item
    print(f"{number}. {name:<8} ${price:.2f}")
print("5. Done")

while True:
    choice = int(input("Choose an item (1-5): "))

    if choice == 5:
        break

    if choice in menu:
        name, price = menu[choice]

        if name in cart:
            cart[name] += 1
        else:
            cart[name] = 1

        total += price
        print(f"Added {name}. Total: ${total:.2f}")
    else:
        print("Invalid choice. Try again.")

print()
print("--- Receipt ---")

for name, quantity in cart.items():
    price = 0

    for item_name, item_price in menu.values():
        if item_name == name:
            price = item_price

    print(f"{name:<8} x{quantity}   ${price * quantity:.2f}")

print("---------------------")
print(f"Total: ${total:.2f}")
print("Thank you!")
