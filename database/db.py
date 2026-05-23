import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

pool = None

async def init_db():

    global pool

    pool = await asyncpg.create_pool(
        os.getenv("DATABASE_URL")
    )

    async with pool.acquire() as conn:

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id BIGINT PRIMARY KEY
        )
        """)

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS resources(
            id SERIAL PRIMARY KEY,
            category TEXT,
            year TEXT,
            branch TEXT,
            semester TEXT,
            subject TEXT,
            file_id TEXT,
            file_name TEXT
        )
        """)
