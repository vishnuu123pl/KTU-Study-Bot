from pyrogram import Client, filters
from config import ADMINS
from database.models import top_requests


@Client.on_message(
    filters.command("topreq") &
    filters.user(ADMINS)
)
async def topreq(_, message):

    rows = await top_requests()

    if not rows:

        await message.reply_text(
            "No requests yet."
        )
        return

    text = "📈 Top Requested Subjects\n\n"

    for row in rows:

        text += (
            f"• {row['subject']} — "
            f"{row['total']} requests\n"
        )

    await message.reply_text(text)
