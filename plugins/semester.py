from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# callback format: scheme_<year>_<cat>   e.g. scheme_2024_materials
@Client.on_callback_query(filters.regex(r"^scheme_(\d+)_(\w+)$"))
async def semester(_, query):
    parts  = query.data.split("_")   # ['scheme','2024','materials']
    year   = parts[1]
    cat    = parts[2]

    rows = [
        [InlineKeyboardButton(f"𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳 {i}", callback_data=f"sem{i}_{year}_{cat}")]
        for i in range(1, 9)
    ]
    rows.append([InlineKeyboardButton("⬅ 𝘉𝘢𝘤𝘬", callback_data=f"cat_{cat}")])

    await query.message.edit_text(
        f"📗 **{year} 𝘚𝘤𝘩𝘦𝘮𝘦**\n\n𝘚𝘦𝘭𝘦𝘤𝘵 𝘚𝘦𝘮𝘦𝘴𝘵𝘦𝘳 👇",
        reply_markup=InlineKeyboardMarkup(rows)
    )
    await query.answer()
