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


def add_member():
    name = input("Member Name: ")
    email = input("Member Email: ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO members (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    print("Member added successfully!")

def show_members():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    if not members:
        print("No members found.")
    else:
        for member in members:
            print(member)

    conn.close()

def loan_book():
    book_id = int(input("Book ID: "))
    member_id = int(input("Member ID: "))
    loan_date = input("Loan Date (YYYY-MM-DD): ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO loans (book_id, member_id, loan_date)
        VALUES (?, ?, ?)
        """,
        (book_id, member_id, loan_date)
    )

    conn.commit()
    conn.close()

    print("Loan recorded successfully!")
  

   
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Add Member")
    print("7. Show Members")
    print("8. Loan Book")
    print("9. Exit")

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
         add_member()

    elif choice == "7":

        show_members()

    elif choice == "8":

        loan_book()

    elif choice == "9":

        print("Goodbye!")

        break

    else:
        print("Invalid choice.")