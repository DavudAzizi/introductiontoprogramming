from cs50 import SQL

db = SQL("sqlite:///../favorites.db")

language = input("Language: ")

rows = db.execute(
    "SELECT COUNT(*) AS count FROM favorites WHERE language = ?",
    language
)

print(f"{language}: {rows[0]['count']}")
