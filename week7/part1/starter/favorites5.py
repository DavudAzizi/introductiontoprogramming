import csv

counts = {}

with open("../favorites.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"]

        if language in counts:
            counts[language] += 1
        else:
            counts[language] = 1

for language in counts:
    print(f"{language}: {counts[language]}")
