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


def add_user(user_id):

    cursor.execute(
        """
        INSERT OR IGNORE INTO users(user_id)
        VALUES(?)
        """,
        (user_id,)
    )

    conn.commit()


def save_resource(
    category,
    year,
    branch,
    semester,
    subject,
    file_id,
    file_name
):

    cursor.execute("""
    INSERT INTO resources(
        category,
        year,
        branch,
        semester,
        subject,
        file_id,
        file_name
    )
    VALUES(?,?,?,?,?,?,?)
    """, (
        category,
        year,
        branch,
        semester,
        subject.lower(),
        file_id,
        file_name
    ))

    conn.commit()


def get_resources(
    category,
    year,
    branch,
    semester,
    subject
):

    cursor.execute("""
    SELECT file_id,file_name
    FROM resources
    WHERE category=?
    AND year=?
    AND branch=?
    AND semester=?
    AND subject=?
    """, (
        category,
        year,
        branch,
        semester,
        subject.lower()
    ))

    return cursor.fetchall()
