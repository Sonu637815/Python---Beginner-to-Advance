# filename for storing books
filename = "library.txt"

# function to load books from file
def load_books():
    try:
        with open(filename, "r") as f:
            books = f.read().splitlines()
        return books
    except FileNotFoundError:
        return []   # agar file exist nahi karti, empty list return karo

# function to save books to file
def save_books(books):
    with open(filename, "w") as f:
        for book in books:
            f.write(book + "\n")

# load existing books
library = load_books()

while True:
    print("\n===== Library Menu =====")
    print("1. Show Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("\nBooks in Library:", library if library else "No books available")

    elif choice == 2:
        book = input("Enter book name: ")
        library.append(book)
        save_books(library)   # save immediately
        print(f"'{book}' added successfully!")

    elif choice == 3:
        book = input("Enter book name to search: ")
        if book in library:
            print(f"'{book}' is available in library ✅")
        else:
            print(f"'{book}' not found ❌")

    elif choice == 4:
        book = input("Enter book name to remove: ")
        if book in library:
            library.remove(book)
            save_books(library)  # save after removal
            print(f"'{book}' removed successfully!")
        else:
            print(f"'{book}' not found, can't remove ❌")

    elif choice == 5:
        save_books(library)
        print("Exiting Library System... Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
