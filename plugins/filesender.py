from pyrogram import Client, filters
from database.models import get_resources
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

        await query.message.reply_text(
            "⚠️ Resource not uploaded yet.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "📩 Request Resource",
                        callback_data=f"request_{category}_{year}_{branch}_{semester}_{subject}"
                    )
               ]
            ])
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
