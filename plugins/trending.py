from pyrogram import Client, filters
from database.models import top_requests


@Client.on_callback_query(
    filters.regex("^top_requests$")
)
async def trending(_, query):

    try:
        await query.answer()
    except:
        pass

    data = await top_requests()

    if not data:

        await query.answer(
            "No requests yet.",
            show_alert=True
        )

        return

    text = (
        "📈 <b>Trending Requests</b>\n\n"
    )

    for idx, row in enumerate(data, 1):

        text += (
            f"{idx}. "
            f"<b>{row['subject'].upper()}</b>"
            f" — {row['total']} requests\n"
        )

    text += (
        "\n━━━━━━━━━━━━━━\n"
        "KTU Study Bot V3"
    )

    await query.message.edit_text(
        text
    )
