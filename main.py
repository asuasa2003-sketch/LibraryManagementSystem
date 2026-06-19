from database import connect

def add_book():
    title = input("Book Title: ")
    author = input("Author: ")
    year = int(input("Year: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (title, author, year)
    )

    conn.commit()
    conn.close()

    print("Book added successfully!")


def show_books():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("No books found.")
    else:
        for book in books:
            print(book)

    conn.close()


def search_book():
    title = input("Enter title: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE title = ?",
        (title,)
    )

    books = cursor.fetchall()

    if not books:
        print("Book not found.")
    else:
        for book in books:
            print(book)

    conn.close()


def update_book():
    book_id = int(input("Enter book ID: "))
    new_title = input("New title: ")
    new_author = input("New author: ")
    new_year = int(input("New year: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE books
        SET title = ?, author = ?, year = ?
        WHERE id = ?
        """,
        (new_title, new_author, new_year, book_id)
    )

    conn.commit()
    conn.close()

    print("Book updated successfully!")


def delete_book():
    book_id = int(input("Enter book ID: "))

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()

    print("Book deleted successfully!")


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        show_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")