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
    ],
    [
        InlineKeyboardButton(
            "💻 𝘚𝘰𝘶𝘳𝘤𝘦 𝘊𝘰𝘥𝘦",
            url="https://github.com/vishnuu123pl/KTU-Study-Bot-V3"
        ),
        InlineKeyboardButton(
            "ℹ️ 𝘈𝘣𝘰𝘶𝘵",
            callback_data="about"
        )
    ]
])

@Client.on_message(filters.command("start"))
async def start(client, message):

    user_id = message.from_user.id

    # Save user to database
    await add_user(user_id)

    # Try to send to log channel, but don't fail if it doesn't work
    try:
        await client.send_message(
            LOG_CHANNEL,
            f"#NewUser\n\n"
            f"ID - {message.from_user.id}\n"
            f"Name - {message.from_user.first_name}"
        )
    except Exception as e:
        print(f"Failed to send to log channel: {e}")

    # Always reply to the user
    await message.reply_photo(
        photo="https://pic-link-bot.lovable.app/i/telegram-1779366829596-64036ff9.jpg",
        caption=START_TEXT,
        reply_markup=START_BUTTONS
    )
