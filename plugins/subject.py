from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA


@Client.on_callback_query(
    filters.regex(
        r"^sub_(\w+)_(sem\d+)_(\d+)_(\w+)$"
    )
)
async def subject(_, query):

    try:
        await query.answer()
    except:
        pass

    _, branch, sem, year, cat = query.data.split("_", 4)

    subjects = DATA.get(
        branch,
        {}
    ).get(
        sem,
        []
    )

    if not subjects:

        try:
            await query.answer(
                "⚠️ 𝘕𝘰 𝘴𝘶𝘣𝘫𝘦𝘤𝘵𝘴 𝘧𝘰𝘶𝘯𝘥.",
                show_alert=True
            )
        except:
            pass

        return

    rows = []

    for idx, sub in enumerate(subjects):

        cb = f"res_{branch}_{sem}_{year}_{cat}_{idx}"

        rows.append([
            InlineKeyboardButton(
                sub[:40],
                callback_data=cb
            )
        ])

    rows.append([
        InlineKeyboardButton(
            "⬅ 𝘉𝘢𝘤𝘬",
            callback_data=f"sem{sem.replace('sem','')}_{year}_{cat}"
        )
    ])

    try:

        await query.message.edit_text(
            "📚 𝘚𝘦𝘭𝘦𝘤𝘵 𝘚𝘶𝘣𝘫𝘦𝘤𝘵",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass
