from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ABOUT_TEXT = """
🎓 <b>KTU Study Bot</b>

Your smart companion for KTU studies.

✨ Features:

📚 Notes
📝 Previous Year Questions
📄 Model Papers
🎥 Video Resources
📊 Admin Upload Panel
🔔 Broadcast System
📖 Semester & Branch Navigation
⚡ Fast file delivery

👨‍💻 Built for KTU students

Version: 3.0
"""

ABOUT_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "📢 Updates",
            url="https://t.me/YOUR_CHANNEL"
        )
    ],
    [
        InlineKeyboardButton(
            "⬅ Back",
            callback_data="back_home"
        )
    ]
])


@Client.on_callback_query(
    filters.regex("^about$")
)
async def about(_, query):

    try:

        await query.message.edit_text(
            ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS
        )

    except:

        pass

    await query.answer()
