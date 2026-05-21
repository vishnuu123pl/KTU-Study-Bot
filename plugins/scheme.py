from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(
    filters.regex(r"^cat_(\w+)$")
)
async def scheme(_, query):

    cat = query.data.split("_",1)[1]

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📘 2024 Scheme",
                callback_data=f"scheme_2024_{cat}"
            )
        ],
        [
            InlineKeyboardButton(
                "📗 2019 Scheme",
                callback_data=f"scheme_2019_{cat}"
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
            "📚 **Select KTU Scheme** 👇",
            reply_markup=buttons
        )

    except:

        pass

    await query.answer()
