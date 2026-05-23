from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from database.models import add_user
from config import LOG_CHANNEL, ADMINS


START_TEXT = """
🎓 <b>𝘒𝘛𝘜 𝘚𝘵𝘶𝘥𝘺 𝘉𝘰𝘵 𝘝3</b>

𝘎𝘦𝘵 <b>𝘕𝘰𝘵𝘦𝘴 • 𝘗𝘠𝘘𝘴 • 𝘔𝘰𝘥𝘦𝘭𝘴 • 𝘝𝘪𝘥𝘦𝘰𝘴</b>
𝘧𝘰𝘳 𝘒𝘛𝘜 𝘴𝘶𝘣𝘫𝘦𝘤𝘵𝘴.

🔎 𝘜𝘴𝘦 /search
𝘧𝘰𝘳 𝘲𝘶𝘪𝘤𝘬 𝘴𝘶𝘣𝘫𝘦𝘤𝘵 𝘴𝘦𝘢𝘳𝘤𝘩.

❓ 𝘕𝘦𝘦𝘥 𝘩𝘦𝘭𝘱?

<b>𝘊𝘭𝘪𝘤𝘬 👉 /help</b>

𝘊𝘩𝘰𝘰𝘴𝘦 𝘢𝘯 𝘰𝘱𝘵𝘪𝘰𝘯 𝘣𝘦𝘭𝘰𝘸 👇
""""


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
