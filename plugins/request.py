from pyrogram import Client, filters
from config import ADMINS


@Client.on_callback_query(
    filters.regex(
        r"^request_(.+)$"
    )
)
async def request_resource(_, query):

    parts = query.data.split("_")

    if len(parts) < 6:

        await query.answer(
            "Invalid request data.",
            show_alert=True
        )

        return

    category = parts[1]
    year = parts[2]
    branch = parts[3]
    semester = parts[4]
    subject = "_".join(parts[5:])

    user = query.from_user

    text = (

        f"📩 Resource Request\n\n"

        f"👤 User: {user.first_name}\n"
        f"🆔 ID: {user.id}\n\n"

        f"📂 Category: {category}\n"
        f"📘 Scheme: {year}\n"
        f"🏫 Branch: {branch.upper()}\n"
        f"📖 Semester: {semester.upper()}\n"
        f"📚 Subject: {subject.upper()}"
    )

    for admin in ADMINS:

        try:

            await _.send_message(
                admin,
                text
            )

        except Exception as e:

            print(e)

    await query.answer(
        "✅ Request sent to admin!",
        show_alert=True
    )
