from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(
    filters.regex(r"^scheme_(\d+)_(\w+)$")
)
async def semester(_, query):

    try:
        await query.answer()
    except:
        pass

    year, cat = query.matches[0].groups()

    rows = []

    # 2-column semester grid
    for i in range(1, 9, 2):

        rows.append([
            InlineKeyboardButton(
                f"📘 𝘚𝘌𝘔 {i}",
                callback_data=f"sem{i}_{year}_{cat}"
            ),
            InlineKeyboardButton(
                f"📗 𝘚𝘌𝘔 {i+1}",
                callback_data=f"sem{i+1}_{year}_{cat}"
            )
        ])

    rows.append([
        InlineKeyboardButton(
            "⬅ 𝘉𝘢𝘤𝘬",
            callback_data=f"cat_{cat}"
        )
    ])

    try:

        await query.message.edit_text(
            f"📚 <b>{year} Scheme</b>\n\n"
            f"Choose your semester 👇",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass
