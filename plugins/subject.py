from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA


@Client.on_callback_query(
    filters.regex(
        r"^sub_(\w+)_(sem\d+)_(\d+)_(\w+)$"
    )
)
async def subject(_, query):

    _, branch, sem, year, cat = query.data.split("_", 4)

    subjects = DATA.get(branch, {}).get(sem, [])

    if not subjects:

        await query.answer(
            "⚠️ No subjects found.",
            show_alert=True
        )
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
            "⬅ Back",
            callback_data=f"sem{sem.replace('sem','')}_{year}_{cat}"
        )
    ])

    try:

        await query.message.edit_text(
            "📚 Select Subject",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass

    await query.answer()
