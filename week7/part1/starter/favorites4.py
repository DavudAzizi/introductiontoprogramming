import csv

python = 0
c = 0
scratch = 0

with open("../favorites.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["language"] == "Python":
            python += 1
        elif row["language"] == "C":
            c += 1
        elif row["language"] == "Scratch":
            scratch += 1

print(f"Python: {python}")
print(f"C: {c}")
print(f"Scratch: {scratch}")
