import sqlite3

DB_NAME = "library.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()

    with open("schema.sql", "r") as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()

    print("Database created successfully!")

if __name__ == "__main__":
    create_tables()