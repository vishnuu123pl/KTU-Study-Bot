from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from database.models import add_user
from config import LOG_CHANNEL, ADMINS


START_TEXT = """
🎓 <b>KTU Study Bot V3</b>

Get <b>Notes • PYQs • Models • Videos</b>
for KTU subjects.

Choose an option below 👇
"""


START_BUTTONS = InlineKeyboardMarkup([

    [
        InlineKeyboardButton(
            "📚 Get Notes / PYQ",
            callback_data="cat_materials"
        )
    ],

    [
        InlineKeyboardButton(
            "🔎 Search Subject",
            switch_inline_query_current_chat="/search "
        )
    ],

    [
        InlineKeyboardButton(
            "ℹ️ About",
            callback_data="about"
        ),

        InlineKeyboardButton(
            "📩 Suggest Resource",
            callback_data="request_menu"
        )
    ],

    [
        InlineKeyboardButton(
            "💻 Source Code",
            url="https://github.com/vishnuu123pl/KTU-Study-Bot-V3"
        )
    ]

])


@Client.on_message(
    filters.command("start")
)
async def start(client, message):

    user_id = message.from_user.id

    # Save user
    try:

        await add_user(
            user_id
        )

    except Exception as e:

        print(
            f"ADD USER ERROR: {e}"
        )

    # Log new users
    try:

        if user_id not in ADMINS:

            await client.send_message(
                LOG_CHANNEL,

                f"#NewUser\n\n"
                f"ID - {user_id}\n"
                f"Name - {message.from_user.first_name}"
            )

    except Exception as e:

        print(
            f"LOG ERROR: {e}"
        )

    # Start message with image
    await message.reply_photo(

        photo=(
            "https://pic-link-bot.lovable.app/i/"
            "telegram-1779366829596-64036ff9.jpg"
        ),

        caption=START_TEXT,

        reply_markup=START_BUTTONS
    )
