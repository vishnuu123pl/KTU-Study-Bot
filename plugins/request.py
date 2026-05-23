from pyrogram import Client, filters
from config import ADMINS
from database.models import add_request


@Client.on_callback_query(
    filters.regex(
        r"^request_(.+)$"
    )
)
async def request_resource(_, query):

    parts = query.data.split("_", 5)

    category = parts[1]
    year = parts[2]
    branch = parts[3]
    semester = parts[4]
    subject = parts[5]

    user = query.from_user

    # SAVE REQUEST TO DB
    await add_request(
        category,
        branch,
        semester,
        subject
    )

    text = (
        f"📩 Resource Request\n\n"
        f"👤 User: {user.first_name}\n"
        f"🆔 ID: {user.id}\n\n"
        f"Category: {category}\n"
        f"Scheme: {year}\n"
        f"Branch: {branch}\n"
        f"Semester: {semester}\n"
        f"Subject: {subject}"
    )

    for admin in ADMINS:

        await _.send_message(
            admin,
            text
        )

    await query.answer(
        "✅ Request sent to admin!",
        show_alert=True
    )
