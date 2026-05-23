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

    files = get_resources(
        category,
        year,
        branch,
        semester,
        subject
    )

    if not files:

        await query.answer(
            "⚠️ 𝘙𝘦𝘴𝘰𝘶𝘳𝘤𝘦 𝘯𝘰𝘵 𝘶𝘱𝘭𝘰𝘢𝘥𝘦𝘥 𝘺𝘦𝘵",
            show_alert=True
        )
        return

    for file_id, file_name in files:

        await query.message.reply_document(
            file_id
        )

    await query.answer()
