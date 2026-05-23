from pyrogram import Client, filters
from database.models import get_resources


@Client.on_callback_query(
    filters.regex(r"^(notes|pyq|model|video)_(.+)$")
)
async def send_resource(_, query):

    try:
        await query.answer()
    except:
        pass

    parts = query.data.split("_")

    category = parts[0]
    year = parts[1]
    branch = parts[2]
    semester = parts[3]
    subject = parts[4]

    files = await get_resources(
        category,
        year,
        branch,
        semester,
        subject
    )

    if len(files) == 0:

        await query.answer(
            "⚠️ 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦 𝘯𝘰𝘵 𝘶𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘺𝘦𝘵",
            show_alert=True
        )
        return

    for row in files:

        if category == "video":

            await query.message.reply_text(
                f"🎥 Video Resource:\n\n{row['file_id']}"
            )

        else:

            await query.message.reply_document(
                row["file_id"]
            )
