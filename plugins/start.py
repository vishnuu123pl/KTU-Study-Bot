from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import add_user
from config import LOG_CHANNEL

START_TEXT = """
🎓 <b>𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 KTU 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵</b>

𝘠𝘰𝘶𝘳 𝘢𝘭𝘭-𝘪𝘯-𝘰𝘯𝘦 𝘴𝘵𝘶𝘥𝘺 𝘤𝘰𝘮𝘱𝘢𝘯𝘪𝘰𝘯 𝘧𝘰𝘳 KTU 𝘴𝘵𝘶𝘥𝘦𝘯𝘵𝘴.
"""

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎓 𝘉.𝘛𝘦𝘤𝘩",
            callback_data="cat_materials"
        )
    ]
])


@Client.on_message(filters.command("start"))
async def start(client, message):

    try:
        await add_user(
            message.from_user.id
        )

    except Exception as e:
        print("ADD USER ERROR:", e)

    try:
        await client.send_message(
            LOG_CHANNEL,
            f"#NewUser\n\n"
            f"ID - {message.from_user.id}\n"
            f"Name - {message.from_user.first_name}"
        )

    except Exception as e:
        print("LOG ERROR:", e)

    await message.reply_photo(
        photo="https://pic-link-bot.lovable.app/i/telegram-1779366829596-64036ff9.jpg",
        caption=START_TEXT,
        reply_markup=START_BUTTONS
    )
