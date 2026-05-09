import csv

counts = {}

with open("../../part1/favorites.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        language = row["language"]

        try:
            counts[language] += 1
        except KeyError:
            counts[language] = 1

for language in sorted(counts, key=counts.get, reverse=True):
    print(f"{language}: {counts[language]}")
