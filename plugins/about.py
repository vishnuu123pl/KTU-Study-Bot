from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(
    filters.regex("^about$")
)
async def about(_, query):

    try:
        await query.answer()
    except:
        pass

    text = (
        "🎓 <b>KTU Study Bot V3</b>\n\n"

        "Your all-in-one KTU study companion.\n\n"

        "✨ <b>Features</b>\n"
        "📄 Notes\n"
        "📝 PYQs\n"
        "📚 Model Papers\n"
        "🎥 Videos\n"
        "📩 Resource Requests\n"
        "🔎 Subject Search\n\n"

        "👨‍💻 <b>Developer</b>\n"
        "@yourusername (𝘝𝘪𝘴𝘩𝘯𝘶)\n\n"

        "━━━━━━━━━━━━━━\n"
        "KTU Study Bot V3"
    )

    buttons = InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "💻 GitHub",
                url="https://github.com/vishnuu123pl/KTU-Study-Bot-V3"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅ Back",
                callback_data="back_home"
            )
        ]

    ])

    try:

        await query.message.edit_text(
            text,
            reply_markup=buttons
        )

    except:
        pass
