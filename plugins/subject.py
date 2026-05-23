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

        await query.answer(
            "⚠️ No subjects found.",
            show_alert=True
        )

        return

    rows = []

    for idx, sub in enumerate(subjects):

        code = sub.split("|")[0].strip()

        rows.append([
            InlineKeyboardButton(
                f"📘 {code.upper()}",
                callback_data=f"res_{branch}_{sem}_{year}_{cat}_{idx}"
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
            f"🏫 <b>{branch.upper()}</b> • "
            f"<b>{sem.upper()}</b>\n"
            f"📚 <b>{year} Scheme</b>\n\n"
            f"Choose a subject 👇",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass
