library = []

while True:
    print("\n1. Add book")
    print("2. View books")
    print("3. Search book")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        title = input("Book title: ")
        author = input("Author: ")

        library.append({
            "title": title,
            "author": author
        })

    elif choice == "2":
        print("\nLibrary:")

        for book in library:
            print(f"{book['title']} by {book['author']}")

    elif choice == "3":
        search = input("Search title: ").lower()

        found = False

        for book in library:
            if search in book["title"].lower():
                print(f"Found: {book['title']} by {book['author']}")
                found = True

        if not found:
            print("Book not found")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
