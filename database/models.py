from database.db import db


async def add_user(user_id):

    async with db.pool.acquire() as conn:

        await conn.execute(
            """
            INSERT INTO users(user_id)
            VALUES($1)
            ON CONFLICT DO NOTHING
            """,
            user_id
        )


async def save_resource(
    category,
    year,
    branch,
    semester,
    subject,
    file_id,
    file_name
):

    async with db.pool.acquire() as conn:

        await conn.execute("""
        INSERT INTO resources(
            category,
            year,
            branch,
            semester,
            subject,
            file_id,
            file_name
        )
        VALUES($1,$2,$3,$4,$5,$6,$7)
        """,
        category,
        year,
        branch,
        semester,
        subject.lower(),
        file_id,
        file_name
        )


async def get_resources(
    category,
    year,
    branch,
    semester,
    subject
):

    async with db.pool.acquire() as conn:

        rows = await conn.fetch("""
        SELECT file_id,file_name
        FROM resources
        WHERE category=$1
        AND year=$2
        AND branch=$3
        AND semester=$4
        AND subject=$5
        """,
        category,
        year,
        branch,
        semester,
        subject.lower()
        )

        return rows


async def delete_resource(
    category,
    year,
    branch,
    semester,
    subject
):

    async with db.pool.acquire() as conn:

        await conn.execute("""
        DELETE FROM resources
        WHERE category=$1
        AND year=$2
        AND branch=$3
        AND semester=$4
        AND subject=$5
        """,
        category,
        year,
        branch,
        semester,
        subject.lower()
        )


async def list_keys():

    async with db.pool.acquire() as conn:

        rows = await conn.fetch("""
        SELECT DISTINCT
        category,year,branch,semester,subject
        FROM resources
        """)

        return rows


async with db.pool.acquire() as conn:

    async with pool.acquire() as conn:

        row = await conn.fetchrow(
            "SELECT COUNT(*) FROM resources"
        )

        return row["count"]


async def get_users():

    async with db.pool.acquire() as conn:

        rows = await conn.fetch(
            "SELECT user_id FROM users"
        )

        return [row["user_id"] for row in rows]
