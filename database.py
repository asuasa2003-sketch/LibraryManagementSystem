import sqlite3

DB_NAME = "library.db"

def connect():
    return sqlite3.connect(DB_NAME)

