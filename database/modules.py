from database.db import conn, cursor


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


def delete_resource(
    category,
    year,
    branch,
    semester,
    subject
):

    cursor.execute("""
    DELETE FROM resources
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

    conn.commit()


def list_keys():

    cursor.execute("""
    SELECT DISTINCT
    category,year,branch,semester,subject
    FROM resources
    """)

    return cursor.fetchall()


def total_resources():

    cursor.execute("""
    SELECT COUNT(*)
    FROM resources
    """)

    return cursor.fetchone()[0]
