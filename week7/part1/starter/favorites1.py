import csv

with open("../favorites.csv") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        language = row[1]
        print(language)
