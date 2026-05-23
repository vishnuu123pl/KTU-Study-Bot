from pyrogram import Client, filters
from config import ADMINS


@Client.on_message(
    filters.command("reply") &
    filters.user(ADMINS)
)
async def reply_user(client, message):

    try:

        _, user_id, text = message.text.split(
            maxsplit=2
        )

        await client.send_message(
            int(user_id),
            f"📩 Admin Reply\n\n{text}"
        )

        await message.reply_text(
            "✅ Reply Sent"
        )

    except Exception as e:

        await message.reply_text(
            f"Usage:\n/reply user_id message\n\n{e}"
        )
