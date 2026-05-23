from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from data import DATA


@Client.on_message(
    filters.command("search")
)
async def search(_, message):

    if len(message.command) < 2:

        await message.reply_text(
            "Usage:\n/search subject"
        )

        return

    query = message.text.split(
        maxsplit=1
    )[1].lower()

    found = False

    for branch in DATA:

        for sem in DATA[branch]:

            subjects = DATA[branch][sem]

            for idx, subject in enumerate(subjects):

                if query in subject.lower():

                    found = True

                    await message.reply_text(

                        f"📚 <b>{subject}</b>\n\n"
                        f"🏫 {branch.upper()} • "
                        f"{sem.upper()}",

                        reply_markup=InlineKeyboardMarkup([

                            [
                                InlineKeyboardButton(
                                    "📚 View Resources",
                                    callback_data=(
                                        f"res_{branch}_"
                                        f"{sem}_"
                                        f"2024_"
                                        f"materials_"
                                        f"{idx}"
                                    )
                                )
                            ]

                        ])
                    )

    if not found:

        await message.reply_text(
            "⚠️ No matching subjects found."
        )
