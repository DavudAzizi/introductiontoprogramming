from cs50 import SQL

db = SQL("sqlite:///../favorites.db")

rows = db.execute(
    "SELECT language, COUNT(*) AS count FROM favorites GROUP BY language ORDER BY count DESC"
)

for row in rows:
    print(f"{row['language']}: {row['count']}")
