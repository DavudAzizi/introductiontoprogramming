# Project 1 — Temperature Converter
# Author: Davud Azizi

choice = input("Convert: (1) Celsius → Fahrenheit  (2) Fahrenheit → Celsius\nChoice: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius}°C")
else:
    print("Invalid choice.")
