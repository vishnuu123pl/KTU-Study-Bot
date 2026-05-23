from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BRANCHES = [
    ("💻 𝘊𝘚𝘌","cse"),
    ("📡 𝘌𝘊𝘌","ece"),
    ("⚡ 𝘌𝘌𝘌","eee"),
    ("🔬 𝘐𝘊𝘌","ice"),
    ("🔧 𝘔𝘌","me"),
    ("🏗 𝘊𝘪𝘷𝘪𝘭","civil")
]


@Client.on_callback_query(
    filters.regex(r"^sem(\d+)_(\d+)_(\w+)$")
)
async def branch(_, query):

    try:
        await query.answer()
    except:
        pass

    sem_no, year, cat = query.matches[0].groups()

    rows = []

    # 2-column layout
    for i in range(0, len(BRANCHES), 2):

        row = []

        for name, code in BRANCHES[i:i+2]:

            row.append(
                InlineKeyboardButton(
                    name,
                    callback_data=f"sub_{code}_sem{sem_no}_{year}_{cat}"
                )
            )

        rows.append(row)

    rows.append([
        InlineKeyboardButton(
            "⬅ 𝘉𝘢𝘤𝘬",
            callback_data="back_home"
        )
    ])

    try:

        await query.message.edit_text(
            f"🏫 <b>Select Branch</b>\n\n"
            f"📖 Semester: <b>SEM {sem_no}</b>\n"
            f"📚 Scheme: <b>{year}</b>\n\n"
            f"Choose your branch 👇",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass
