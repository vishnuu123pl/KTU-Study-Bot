from pyrogram import Client, filters
from data import DATA


@Client.on_message(
    filters.command("search")
)
async def search(_, message):

    if len(message.command) < 2:

        await message.reply_text(
            "Usage:\n/search subject_code"
        )

        return

    query = message.text.split(
        maxsplit=1
    )[1].lower()

    results = []

    for branch in DATA:

        for sem in DATA[branch]:

            for subject in DATA[branch][sem]:

                if query in subject.lower():

                    results.append(
                        f"📚 <b>{subject}</b>\n"
                        f"🏫 {branch.upper()} • "
                        f"{sem.upper()}"
                    )

    if not results:

        await message.reply_text(
            "⚠️ No matching subjects found."
        )

        return

    text = (
        "🔎 <b>Search Results</b>\n\n" +
        "\n\n".join(results[:15])
    )

    await message.reply_text(text)
