from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(
    filters.regex(r"^cat_(\w+)$")
)
async def scheme(_, query):

    try:
        await query.answer()
    except:
        pass

    cat = query.data.split("_",1)[1]

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📘 2024 𝘚𝘤𝘩𝘦𝘮𝘦",
                callback_data=f"scheme_2024_{cat}"
            )
        ],
        [
            InlineKeyboardButton(
                "📗 2019 𝘚𝘤𝘩𝘦𝘮𝘦",
                callback_data=f"scheme_2019_{cat}"
            )
        ],
        [
            InlineKeyboardButton(
                "⬅ 𝘉𝘢𝘤𝘬",
                callback_data="back_home"
            )
        ]
    ])

    try:

        await query.message.edit_text(
            """📚 Select KTU Scheme

Choose your academic scheme 👇""",
            reply_markup=buttons
        )

    except:
        pass
