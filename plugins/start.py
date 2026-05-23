from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import add_user
from config import LOG_CHANNEL, ADMINS

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

    # Save user
    try:
        await add_user(user_id)

    except Exception as e:
        print(f"ADD USER ERROR: {e}")

    # Log only non-admin users
    try:

        if user_id not in ADMINS:

            await client.send_message(
                LOG_CHANNEL,
                f"#NewUser\n\n"
                f"ID - {user_id}\n"
                f"Name - {message.from_user.first_name}"
            )

    except Exception as e:
        print(f"LOG ERROR: {e}")

    # Always respond - try with photo first, fallback to text if photo fails
    try:
        # Try using a file_id if you have one, or a reliable image URL
        # For now, we'll use the original URL with fallback
        await message.reply_photo(
            photo="https://pic-link-bot.lovable.app/i/telegram-1779366829596-64036ff9.jpg",
            caption=START_TEXT,
            reply_markup=START_BUTTONS
        )
    except Exception as e:
        print(f"PHOTO ERROR: {e}")
        # Fallback to text message if photo fails
        try:
            await message.reply_text(
                text=START_TEXT,
                reply_markup=START_BUTTONS,
                disable_web_page_preview=True
            )
        except Exception as e2:
            print(f"TEXT FALLBACK ERROR: {e2}")
            # Last resort - simple text without buttons
            await message.reply_text(START_TEXT)
