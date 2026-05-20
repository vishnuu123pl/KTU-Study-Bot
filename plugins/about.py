from pyrogram import Client, filters

@Client.on_callback_query(
    filters.regex("^about$")
)
async def about(_, query):

    text = """
🎓 KTU Study Bot

📚 Notes
📝 PYQ
📄 Model Papers

Built for KTU students.

Developed with ❤️
"""

    await query.message.edit_text(text)

    await query.answer()
