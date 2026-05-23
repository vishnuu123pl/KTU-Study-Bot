import sqlite3

conn = sqlite3.connect(
    "ktu_bot.db",
    check_same_thread=False
)

cursor = conn.cursor()

def init_db():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        year TEXT,
        branch TEXT,
        semester TEXT,
        subject TEXT,
        file_id TEXT,
        file_name TEXT
    )
    """)

    conn.commit()
