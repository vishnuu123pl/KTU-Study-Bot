from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BRANCHES = [
    ("💻 𝘊𝘚𝘌","cse"),
    ("📡 𝘌𝘊𝘌","ece"),
    ("⚡ 𝘌𝘌𝘌","eee"),
    ("🔬 𝘐𝘊𝘌", "ice"),
    ("🔧 𝘔𝘌","me"),
    ("🏗 𝘊𝘪𝘷𝘪𝘭","civil")
]


@Client.on_callback_query(
    filters.regex(r"^sem(\d+)_(\d+)_(\w+)$")
)
async def branch(_, query):

    sem_no, year, cat = query.matches[0].groups()

    rows=[]

    for name, code in BRANCHES:

        rows.append([
            InlineKeyboardButton(
                name,
                callback_data=f"sub_{code}_sem{sem_no}_{year}_{cat}"
            )
        ])

    rows.append([
        InlineKeyboardButton(
            "⬅ 𝘉𝘢𝘤𝘬",
            callback_data="back_home"
        )
    ])

    try:

        await query.message.edit_text(
            f"📘 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳 {sem_no}\n\n𝘚𝘦𝘭𝘦𝘤𝘵 𝘉𝘳𝘢𝘯𝘤𝘩 👇",
            reply_markup=InlineKeyboardMarkup(rows)
        )

    except:
        pass

    await query.answer()
