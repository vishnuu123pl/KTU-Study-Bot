from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA


@Client.on_callback_query(
    filters.regex(
        r"^res_(\w+)_sem(\d+)_(\d+)_(\w+)_(\d+)$"
    )
)
async def resources(_, query):

    try:
        await query.answer()
    except:
        pass

    _, branch, sem_str, year, cat, idx_str = query.data.split("_", 5)

    sem = sem_str
    sem_no = sem.replace("sem", "")

    idx = int(idx_str)

    subjects = DATA.get(
        branch,
        {}
    ).get(
        sem,
        []
    )

    if idx >= len(subjects):

        await query.answer(
            "⚠️ Subject not found.",
            show_alert=True
        )

        return

    subject_name = subjects[idx]

    parts = subject_name.split("|")

    subject_code = parts[0].strip().lower()

    subject_title = (
        parts[1].strip()
        if len(parts) > 1
        else subject_code.upper()
    )

    text = (
        f"📚 <b>{subject_code.upper()}</b>\n"
        f"{subject_title}\n\n"

        f"🏫 <b>{branch.upper()}</b> • "
        f"<b>SEM {sem_no}</b>\n"

        f"📘 <b>{year} Scheme</b>\n\n"

        f"Choose resource 👇"
    )

    buttons = InlineKeyboardMarkup([

        [
            InlineKeyboardButton(
                "📄 Notes",
                callback_data=f"notes_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),
            InlineKeyboardButton(
                "📝 PYQ",
                callback_data=f"pyq_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],

        [
            InlineKeyboardButton(
                "📚 Models",
                callback_data=f"model_{year}_{branch}_sem{sem_no}_{subject_code}"
            ),
            InlineKeyboardButton(
                "🎥 Videos",
                callback_data=f"video_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],

        [
            InlineKeyboardButton(
                "📩 Request Resource",
                callback_data=f"request_notes_{year}_{branch}_sem{sem_no}_{subject_code}"
            )
        ],

        [
            InlineKeyboardButton(
                "⬅ Back",
                callback_data=f"sub_{branch}_{sem}_{year}_{cat}"
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
