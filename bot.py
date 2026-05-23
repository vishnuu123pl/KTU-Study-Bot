from pyrogram import Client, idle
from pyrogram import utils as pyroutils
from config import API_ID, API_HASH, BOT_TOKEN, ADMINS
from database.db import init_db
import asyncio
import logging


# asyncio warning fix
logging.getLogger(
    "asyncio"
).setLevel(
    logging.CRITICAL - 1
)

# Pyrogram peer id fix
pyroutils.MIN_CHAT_ID = -999999999999
pyroutils.MIN_CHANNEL_ID = -100999999999999


app = Client(
    "KTUStudyBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)


async def main():

    await init_db()

    await app.start()

    print("✅ Bot Started Successfully")

    for admin in ADMINS:

        try:

            await app.send_message(
                admin,
                "🔄 Bot Restarted Successfully"
            )

        except Exception as e:

            print(e)

    await idle()


if __name__ == "__main__":

    asyncio.run(main())
