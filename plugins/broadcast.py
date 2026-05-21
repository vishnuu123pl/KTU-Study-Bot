from pyrogram import Client, filters
import json
import asyncio
from config import ADMINS

@Client.on_message(
    filters.command("broadcast") &
    filters.user(ADMINS)
)
async def broadcast(_, message):

    if len(message.command) < 2:

        await message.reply_text(
            "𝘜𝘴𝘢𝘨𝘦:\n/broadcast Your message"
        )

        return

    text = message.text.split(
        maxsplit=1
    )[1]

    try:

        with open("users.json") as f:

            users = json.load(f)

    except:

        users = []

    sent = 0
    failed = 0

    status = await message.reply_text(
        "📢 𝘉𝘳𝘰𝘢𝘥𝘤𝘢𝘴𝘵𝘪𝘯𝘨..."
    )

    for user in users:

        try:

            await _.send_message(
                user,
                f"📢 𝘜𝘱𝘥𝘢𝘵𝘦\n\n{text}"
            )

            sent += 1

            await asyncio.sleep(0.2)

        except:

            failed += 1

    await status.edit_text(

        f"✅ 𝘉𝘳𝘰𝘢𝘥𝘤𝘢𝘴𝘵 𝘊𝘰𝘮𝘱𝘭𝘦𝘵𝘦\n\n"
        f"𝘚𝘦𝘯𝘵: {sent}\n"
        f"𝘍𝘢𝘪𝘭𝘦𝘥: {failed}"

    )
